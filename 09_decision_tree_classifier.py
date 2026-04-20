import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "Texture": [0, 0, 1, 1, 1],
    "Weight": [150, 170, 160, 190, 200],
    "Fruit": ["Apple", "Apple", "Orange", "Melon", "Melon"]
})

m = DecisionTreeClassifier().fit(df[["Texture", "Weight"]], df["Fruit"])

print("Decision Tree Classifier Rules:\n")
print(export_text(m, feature_names=["Texture", "Weight"]))

plot_tree(m, feature_names=["Texture", "Weight"])
plt.show() 
