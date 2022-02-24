import seaborn as sns
tips = sns.load_dataset('tips')
print(tips)

g = sns.lmplot(x="total_bill",y="tip",data=tips);
g.fig.suptitle('Relationship b/w tip and total_bill [Scatter Plot + Regression Line]',y=1.05);