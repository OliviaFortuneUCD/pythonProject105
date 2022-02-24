import pandas as pd

import matplotlib.pyplot as plt



#load in the dataframe
df = pd.read_csv("Wine.csv", index_col=0)

country = df.groupby("country")

plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")
plt.show()