import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
df=pd.read_csv('weatherAUS.csv')
print(df.head())

df = pd.read_csv('weatherAUS.csv')

# drop rows missing the columns we actually need — including the raw target — BEFORE encoding
df.dropna(subset=['MinTemp','MaxTemp','Rainfall','WindGustSpeed','WindSpeed9am',
                   'WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am',
                   'Pressure3pm','Temp9am','Temp3pm','RainTomorrow'], inplace=True)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['RainTomorrow_encoded'] = le.fit_transform(df['RainTomorrow'])

X = df[['MinTemp','MaxTemp','Rainfall','WindGustSpeed','WindSpeed9am','WindSpeed3pm',
        'Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Temp9am','Temp3pm']]
y = df['RainTomorrow_encoded']

print('X:', X)
print('y:',y)
SEED=100
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=SEED)
print(X_train)
print(y_train)

from sklearn.preprocessing import StandardScaler
scale=StandardScaler()
X_train_scaled=scale.fit_transform(X_train)
X_test_scaled=scale.transform(X_test)

log=LogisticRegression()
log.fit(X_train_scaled,y_train)
y_pred=log.predict(X_test_scaled)

print('Accuracy:', metrics.accuracy_score(y_test,y_pred))

cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()
read=input('wait a mint')


from sklearn.tree import DecisionTreeClassifier, export_graphviz
from six import StringIO
import pydotplus
from IPython.display import Image

# limit depth: an unrestricted tree on this dataset will grow to hundreds of
# nodes and produce an unreadable (and slow-to-render) image
clf = DecisionTreeClassifier(max_depth=4, random_state=SEED)
clf.fit(X_train, y_train)  # trees don't need scaled features -- use X_train directly, not X_train_scaled

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
graph.write_png("rain_tree.png")   # renamed from "iris_tree.png" -- that name was leftover from the tutorial this snippet is based on

Image(graph.create_png())