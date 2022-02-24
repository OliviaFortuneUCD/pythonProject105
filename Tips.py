import seaborn as sns
tips = sns.load_dataset('tips')
print(tips)


g = sns.catplot(x="day",kind='count',order=['Thur','Fri','Sun','Sat'],data=tips);
g.fig.suptitle("Frequency of days in the tips dataset [Count Plot]",y=1.05);