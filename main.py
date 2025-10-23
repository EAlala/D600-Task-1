import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D600 Task 1/D600 Task 1 Dataset 1 Housing Information.csv")

#Descriptive stats
print("Do you want to run descriptive stats? (Yes/No)")
while True:
    user_response = input("")
    if user_response == "Yes":
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
        print("\nDo you want to run univariate visuals? (Yes/No)")
        while True:
            user_response = input("")
            if user_response == "Yes":
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
                        analysis_data_set[var].hist(bins=30, ax=axes[i], edgecolor='black')
                        axes[i].set_title(f'Distribution of {var}')
                        axes[i].set_xlabel(var)
                        axes[i].set_ylabel('Frequency')

                #Hide empty subplots
                for j in range(len(num_vars), len(axes)):
                    axes[j].set_visible(False)

                #Show visual
                plt.tight_layout()
                plt.show()
                break
            else:
                print("\n Okay moving on")
                break
        
        #Bivariate visuals
        print("\nDo you want to run bivariate visuals? (Yes/No)")
        while True:
            user_response = input("")
            if user_response == "Yes":

                #Create scatter plot
                fig, axes = plt.subplots(4, 4, figsize=(20, 16))
                fig.suptitle('Bivariate Analysis: Relationship of Independent Variables with Price', fontsize=16)
                axes = axes.ravel()
                
                #Scatter plot for each numerical variable against price
                for i, var in enumerate(num_vars[1:]):  # Start from 1 to skip 'Price' itself
                    if i < len(axes):
                        axes[i].scatter(analysis_data_set[var], analysis_data_set['Price'], alpha=0.5)
                        axes[i].set_title(f'Price vs {var}')
                        axes[i].set_xlabel(var)
                        axes[i].set_ylabel('Price')

                #Hide any empty subplots
                for j in range(len(num_vars)-1, len(axes)):
                    axes[j].set_visible(False)
                
                #Show visual
                plt.tight_layout()
                plt.show()
                break

            else:
                print("\n Okay moving on")
                break

        
        #Categorical variables vs price
        print("\nDo you want to run categorical variables vs price visuals? (Yes/No)")
        while True:
            user_response = input("")
            if user_response == "Yes":

                #Create box plot
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

                
                break
            else:
                print("\n Okay moving on")
                break
