import seaborn as sns
tips = sns.load_dataset('tips')
print(tips)

g = sns.catplot(x="day",y="tip",kind='bar',hue='smoker',order=['Thur','Fri','Sun','Sat'],ci=False,data=tips);
g.fig.suptitle('Tips by day with smoker/non-smoker subgroup [Grouped Bar Plot]',y=1.05);