import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)



from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(X_train,y_train)
y_pred=log.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[ "setosa", "versicolor", "virginica"]
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix: Model Performance")
plt.show()
read=input('wait for me')


from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from io import StringIO
from IPython.display import Image
import pydotplus

dse = DecisionTreeClassifier(random_state=42)

dse.fit(X_train, y_train)

y_pred1 = dse.predict(X_test)

cm = confusion_matrix(y_test, y_pred1)

print(cm)
print(classification_report(y_test, y_pred1))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["setosa", "versicolor", "virginica"]
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Decision Tree: Confusion Matrix")
plt.show()

read = input("wait for me")




from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))



from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print('Acoraccy:', accuracy_score(y_test,y_pred))
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))
disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["setosa", "versicolor", "virginica"])
disp.plot(cmap=plt.cm.Blues)
plt.title('decision tree:', 'confusion metrix')
plt.show()