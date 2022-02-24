import pandas as pd

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


#load in the dataframe
df = pd.read_csv("Wine.csv", index_col=0)

country = df.groupby("country")

#start with one review:
text = df.description[0]

#Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

#Display the Generated image:
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()