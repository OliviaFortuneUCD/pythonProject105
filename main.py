import warnings
import seaborn as sns
# Convert dataset to pandas dataframes
import pandas as pd
df = pd.read_csv("nyt1.csv")



# Create a new variable 'age_group' to categorize users by age
bins = [0, 18, 25, 35, 45, 55, 65, 110]
labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['age_group'] = pd.cut(df.Age, bins, labels = labels,include_lowest = True)

warnings.filterwarnings('ignore')
# Set default theme and figure size
sns.set_theme()
sns.set(rc={'figure.figsize':(20,10)})
sns.countplot(x='age_group', hue='Gender', data=df)