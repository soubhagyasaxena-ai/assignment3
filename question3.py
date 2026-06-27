# using pandas library 
import pandas as pd;
# to read the data in CSV file 
data = pd.read_csv("data.csv")
# extract the column data
column1 = data["column1"]
column2 = data["column2"]
# correlation the column1 and column2 
correlation=column1.corr(column2)
# print the exact value 
print("Correlation =",correlation)
