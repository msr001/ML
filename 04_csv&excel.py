
import pandas as pd

#File path should look like C:\Users\Downloads\csv_data.txt and C:\Users\Downloads\excel_data.xlsx

csv_data = pd.read_csv(r"paste-entire-csv-file-path-here")
print("\n----------- CSV Data : ----------\n")
print(csv_data)
print("\n----------- CSV describe: ----------\n")
print(csv_data.describe())
print("\n----------- CSV Dtypes: ----------\n")
print(csv_data.dtypes)

excel_data = pd.read_excel(r"paste-entire-excel-file-path-here")
print("\n----------- Excel Data : ----------\n")
print(excel_data)
print("\n----------- Excel describe: ----------\n")
print(excel_data.describe())
print("\n----------- Excel Dtypes: ----------\n")
print(excel_data.dtypes)
