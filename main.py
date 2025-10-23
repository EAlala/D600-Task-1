import pandas as pd

#Read data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D600 Task 1/D600 Task 1 Dataset 1 Housing Information.csv")


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