import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('Iris.csv')
print(df.head())
print('df.shape():', df.shape)

from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['class_encoded'] = le.fit_transform(df['Species'])
print("class label mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df['Species'].head())





y=df['class_encoded']
X=df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

print('y:', y)
print('X:', X)

SEED=50
from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=SEED)
print(X_train)
print(y_train)


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=SEED)
clf=clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print("Acurracy:", metrics.accuracy_score(y_test,y_pred))


from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()

export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=X.columns,
    class_names=le.classes_
)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("iris_tree.png")

Image(graph.create_png())


from sklearn.metrics import  classification_report,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))
read=input('wait a mint')