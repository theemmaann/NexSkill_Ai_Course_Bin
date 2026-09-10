import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')




sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='darkgrid', rc={'axes.facecolor':'grey', 'grid.color':'white'})
sns.lineplot(x='x', y='y', data=data)
plt.show()

df= pd.read_csv('FastFoodRestaurants (1).csv', delimiter=',', parse_dates=[5], date_format={'date_added': '%m-%d-%Y'}, index_col='city')
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)

sns.set_theme(style='whitegrid')
g=sns.displot(data=dffilter, x='country', y='city', hue='keys', kind='hist')
g.figure.suptitle("sns.displot (data=dffilter, x= country, hue=key, kind='hist')")
g.figure.show()
read=input("Wait for me....")


g=sns.kdeplot(data=dffilter, x="latitude")
g.figure.suptitle("sns.kdeplot(data=dffilter, x='address')")
g.figure.show()
read=input("Wait for me....")

g=sns.histplot(data=dffilter, x='longitude', y='latitude', hue='longitude', multiple="stack")
g.figure.suptitle("sns.histplot(date=dffilter, x=longitude, y=latitude, hue=longitude, multiple=stack)")
g.figure.show()
read=input("what for me....")

g=sns.scatterplot(x='longitude', y='latitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x=longitude, y=latitude, data=dffilter )")
g.figure.show()
read=input("what for me....")

g=sns.lineplot(x='longitude', y='latitude', data=dffilter)
g.figure.suptitle("sns.suptitle(x=longitude, y=latitude, data=dffilter)")
g.figure.show()
read=input("what for me ")
g=sns.barplot(data=dffilter, x='longitude', y='postalCode', legend=False)
g.figure.suptitle("sns.suptitle(x=latitude, y=longitude, data=dffilter)")
g.figure.show()
read=input("what for me")

g=sns.catplot(data=dffilter, x='postalCode', y='latitude')
g.figure.suptitle("sns.catplot(data=dffilter, x=postalcode, y=latitude)")
g.figure.show()
read=input("what fo me")
print(dffilter.columns.tolist())
glue=dffilter.pivot(columns="latitude", values="longitude")


g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-glue=dffilter.pivot(columns=latitude, values=longitude)")
g.figure.show()
read=input("what for me")