import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df=pd.DataFrame({
"exam1":[35,40,45,50,55,60,65,70,75,80],
"exam2":[40,45,50,55,60,65,70,75,80,85],
"result":["fail","fail","fail","pass","pass","pass","pass","pass","pass","pass"]
})

m=KNeighborsClassifier(3).fit(df[["exam1","exam2"]],df["result"])

print("Accuracy on test set 1\n")
s1=int(input("Exam score 1 :\n"))
s2=int(input("Exam score 2 :\n"))

new_data=pd.DataFrame([[s1,s2]],columns=["exam1","exam2"])

predict=m.predict(new_data)[0]

print("Based on the exam score, the student is predict to",predict)
