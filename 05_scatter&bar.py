
import pandas as pd
import matplotlib.pyplot as plt
csv_data= pd.read_csv(r"paste-entire-csv-file-path-here")

plt.scatter(csv_data["Age"],csv_data["Score"])
plt.grid()
plt.title("Age vs Score")
plt.show()

plt.bar(csv_data.index + 1, csv_data["Score"])
plt.title("Student Index Number vs Score")
plt.show()
