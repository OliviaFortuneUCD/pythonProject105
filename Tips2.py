import seaborn as sns
tips = sns.load_dataset('tips')
print(tips)

g = sns.jointplot(x="total_bill",y='tip',data=tips,kind='kde');
g.fig.suptitle('Density distribution among tips and total_bill [Joint Plot]',y=1.05);