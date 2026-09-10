import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.DataFrame({'x':np.arange(100), 'y':np.random.rand(100).cumsum()})
sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
sns.set_theme(style='dark')
plt.show()


sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show

sns.lineplot(x='x', y='y', data=data)
sns.set_theme(style='white')
plt.show()

sns.lineplot(x='x', y='y', data=data)
sns.set_theme(style='whitegrid')
plt.show

df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',',parse_dates=[5], date_format={'date_added': '%m-%d-%Y'}, index_col='Address')
print(df.dtypes)
d=dffilter=df.head(40)
dffilter100=df.head(100)

sns.set_theme(style='whitegrid')
g=sns.displot(data=dffilter, x='List Year', y='Address')
g.figure.suptitle("sns.displot(data=dffilter x=List Year y=Address)")
g.figure.show()
read=input('wait for me')

g=sns.kdeplot(data=dffilter, x='List Year',y='Sales Ratio')
g.figure.suptitle("sns.kdeplot(data=dffilter x=Sale Amount y=Sales Ratio)")
g.figure.show()
read=input("wait for me")


g=sns.histplot(data=dffilter, x='Address', y='Sales Ratio')
g.figure.suptitle("sns.hisplot(data=dffilter x=Address y=Sale Amount)")
g.figure.show()
read=input("wait for me")


g=sns.scatterplot(data=dffilter, x='Sales Ratio', y='Address')
g.figure.suptitle("sns.scatterplot (data=dffilter, x=Sales Ratio y=Address)")
g.figure.show()
read=input("wait for me")

g=sns.lineplot(data=dffilter, x='Address', y='List Year')
g.figure.suptitle("sns.linelot(data=dffilter, x=Addredd y=List Year)")
g.figure.show()
read=input("wair for me")

g=sns.barplot(data=dffilter, x='List Year', y='Sales Ratio')
g.figure.suptitle("sns.barplot(data=barplot x=Sales Ratio y=Address)")
g.figure.show()
read=input("wait for me")

g=sns.catplot(data=dffilter, x='Address', y='Sales Ratio')
g.figure.suptitle("sns.catplot(data=dffilter x=Address y=Sales Rato)")
g.figure.show()
read=input("wait for me")


glue=dffilter.pivot(columns="List Year", values="Sales Ratio")
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(data=dffilter x=Address y=Sales Ratio)")
g.figure.show()
read=input("wait for me")