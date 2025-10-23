import pandas as pd

#Read data set
data_set = pd.read_csv("C:/Users/yeai2_6rsknlh/OneDrive/Visual/D600 Task 1/D600 Task 1 Dataset 1 Housing Information.csv")

#Define variables
dep_var = "Price"
indep_vars = ["SquareFootage", "NumBathrooms", "NumBedrooms", "BackyardSpace",
    "CrimeRate", "SchoolRating", "AgeOfHome", "DistanceToCityCenter",
    "EmploymentRate", "PropertyTaxRate", "RenovationQuality", "LocalAmenities",
    "TransportAccess", "Fireplace", "Garage"]

