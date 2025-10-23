import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error

#Read data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D600 Task 1/D600 Task 1 Dataset 1 Housing Information.csv")

#Descriptive stats
#Define variables
dep_var = "Price"
indep_vars = ["SquareFootage", "NumBathrooms", "NumBedrooms", "BackyardSpace",
    "CrimeRate", "SchoolRating", "AgeOfHome", "DistanceToCityCenter",
    "EmploymentRate", "PropertyTaxRate", "RenovationQuality", "LocalAmenities",
    "TransportAccess", "Fireplace", "Garage"]

#New dataframe 
analysis_data_set = data_set[[dep_var] + indep_vars]

#Descriptive stats
desc_stats = analysis_data_set.describe(include="all").transpose()

#Mode and range for table
desc_stats["mode"] = analysis_data_set.mode().iloc[0]
desc_stats["range"] = desc_stats["max"] - desc_stats["min"]

#Clearer presentation
final_stats = desc_stats[["count", "mean", "mode", "std", "min", "max", "range"]]

#Display
print(final_stats.round(2))

print(f"\n{analysis_data_set["Fireplace"].value_counts()}")
print(f"\n{analysis_data_set["Garage"].value_counts()}")
       
        
#Univariate visuals
#Visual style
sns.set_theme(style = "whitegrid")

#Histogram of numerical variables
fig, axes = plt.subplots(4, 4, figsize=(20, 16))
fig.suptitle("Univariate Distributions of Numerical Variables", fontsize=16)
axes = axes.ravel()

#Numberical varbiables to plot
num_vars = ["SquareFootage", "NumBathrooms", "NumBedrooms", "BackyardSpace",
            "CrimeRate", "SchoolRating", "AgeOfHome", "DistanceToCityCenter",
            "EmploymentRate", "PropertyTaxRate", "RenovationQuality", "LocalAmenities",
            "TransportAccess", "Fireplace", "Garage"]

#Plot Hisogram for each variable
for i,var in enumerate(num_vars):
    if i < len(axes):
        analysis_data_set[var].hist(bins=30, ax=axes[i], edgecolor="black")
        axes[i].set_title(f"Distribution of {var}")
        axes[i].set_xlabel(var)
        axes[i].set_ylabel("Frequency")

#Hide empty subplots
for j in range(len(num_vars), len(axes)):
    axes[j].set_visible(False)

#Show visual
plt.tight_layout()
plt.show()

#Bivariate visuals
#Create scatter plot
fig, axes = plt.subplots(4, 4, figsize=(20, 16))
fig.suptitle("Bivariate Analysis: Relationship of Independent Variables with Price", fontsize=16)
axes = axes.ravel()

#Scatter plot for each numerical variable against price
for i, var in enumerate(num_vars[1:]):  # Start from 1 to skip "Price" itself
    if i < len(axes):
        axes[i].scatter(analysis_data_set[var], analysis_data_set["Price"], alpha=0.5)
        axes[i].set_title(f"Price vs {var}")
        axes[i].set_xlabel(var)
        axes[i].set_ylabel("Price")

#Hide any empty subplots
for j in range(len(num_vars)-1, len(axes)):
    axes[j].set_visible(False)

#Show visual
plt.tight_layout()
plt.show()


#Categorical variables vs price
#Create box plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

#Boxplot for Fireplace
sns.boxplot(data = analysis_data_set, x="Fireplace", y="Price", ax=ax1)
ax1.set_title("Price Distribution by Fireplace Presence")

#Boxplot for Garage
sns.boxplot(data = analysis_data_set, x="Garage", y="Price", ax=ax2)
ax2.set_title("Price Distribution by Garage Presence")

#Show visuals
plt.tight_layout()
plt.show()


#Data analysis and report  
#Create copy of analysis_data_set to encoded.
analysis_data_set_encoded = analysis_data_set.copy()

#Convert categorical variables to numerical
analysis_data_set_encoded["Fireplace"] = analysis_data_set_encoded["Fireplace"].map({"Yes": 1, "No": 0})
analysis_data_set_encoded["Garage"] = analysis_data_set_encoded["Garage"].map({"Yes": 1, "No": 0})

#Define X (features) and y (target)
X = analysis_data_set_encoded.drop("Price", axis=1)
Y = analysis_data_set_encoded["Price"]

#Split the data (80% training, 20% testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"\nTraining set size: {X_train.shape[0]} samples")
print(f"\nTest set size: {X_test.shape[0]} samples")

#Save datasets to files
X_train.to_csv('training_features.csv', index=False)
Y_train.to_csv('training_target.csv', index=False)
X_test.to_csv('test_features.csv', index=False)
Y_test.to_csv('test_target.csv', index=False)

print("\nTraining and test datasets saved to files.")

#All features
features = list(X_train.columns)
optimal_features = features.copy()

#Backward elimination
for i in range(len(features)):
    X_temp = X_train[optimal_features]
    X_temp = sm.add_constant(X_temp)
    model = sm.OLS(Y_train, X_temp).fit()

    #Find featuers with highest p-value
    p_values = model.pvalues[1:]  # Skip intercept
    max_p = p_values.max()
    if max_p > 0.05:
        # Remove feature with p-value > 0.05
        worst_feature = p_values.idxmax()
        optimal_features.remove(worst_feature)
        print(f"Removed {worst_feature} (p-value: {max_p:.4f})")
    else:
        break

#Final optimized model
X_optimal = sm.add_constant(X_train[optimal_features])
final_model = sm.OLS(Y_train, X_optimal).fit()

print("\nOPTIMIZED MODEL SUMMARY:")
print(f"R-squared: {final_model.rsquared:.4f}")
print(f"Adjusted R-squared: {final_model.rsquared_adj:.4f}")
print(f"F-statistic: {final_model.fvalue:.4f}")
print(f"nProb (F-statistic): {final_model.f_pvalue:.4f}")

print("\nCOEFFICIENTS AND P-VALUES:")
results_df = pd.DataFrame({
    'Coefficient': final_model.params[1:],
    'P-value': final_model.pvalues[1:]
}, index=optimal_features)
print(results_df.round(4))

#