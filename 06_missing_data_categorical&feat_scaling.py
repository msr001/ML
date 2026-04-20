import pandas as pd
from sklearn.preprocessing import StandardScaler

df=pd.DataFrame({
    "age":[10,15,20,None],
    "gender":["male","female","female","male"],
    "income":[10000,20000,None,30000]
})

print("Data after handling missing data :\n")
df["age"]=df["age"].fillna(df["age"].mean())
df["income"]=df["income"].fillna(df["income"].mean())
print(df)

print("Data after handling categorical variable is : \n" )
df=pd.get_dummies(df,columns=["gender"],dtype=int)
print(df)

print("Data after feature scaling is :\n")
scaler=StandardScaler()
df[["age","income"]]=scaler.fit_transform(df[["age","income"]])
print(df)
