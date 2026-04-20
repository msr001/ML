import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "size": [1000, 1200, 1400, 1600, 1800, 2000],
    "bedrooms": [2, 2, 3, 3, 4, 4],
    "price": [25000, 30000, 35000, 45000, 50000, 55000]
})

m = LinearRegression().fit(df[["size", "bedrooms"]], df["price"])

s = int(input("Enter the size of the house in sqft: "))
b = int(input("Enter the number of bedrooms: "))

new_data = pd.DataFrame([[s, b]], columns=["size", "bedrooms"])
predict = m.predict(new_data)[0]

print(f"Predicted price for a house with size {s} sqft and {b} bedrooms: Rs.{predict}")
