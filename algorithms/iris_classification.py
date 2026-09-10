"""
Iris Flower Classification - Beginner Machine Learning Project
=================================================================
Goal: Predict the species of an Iris flower (Setosa, Versicolor, Virginica)
using 4 measurements: sepal length, sepal width, petal length, petal width.

This script follows the standard ML workflow:
1. Load data
2. Explore data (EDA)
3. Prepare data (split + scale)
4. Train models
5. Evaluate models
6. Visualize results
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # safe non-interactive backend; remove this line if running in Jupyter/Colab
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# -----------------------------
# STEP 1: Load Dataset
# -----------------------------
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["species"] = iris.target
df["species_name"] = df["species"].map(dict(enumerate(iris.target_names)))

print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nClass distribution:")
print(df["species_name"].value_counts())


# -----------------------------
# STEP 2: Explore Data (EDA)
# -----------------------------
# Pairplot shows how well the 3 species separate using each pair of features
sns.pairplot(df, hue="species_name", vars=iris.feature_names)
plt.savefig("iris_pairplot.png", dpi=120, bbox_inches="tight")
plt.close()
print("\nSaved iris_pairplot.png")


# -----------------------------
# STEP 3: Prepare Data
# -----------------------------
X = df[iris.feature_names]
y = df["species"]

# 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling helps Logistic Regression and KNN (distance/gradient based).
# Decision Trees don't need it, but scaling never hurts them either.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -----------------------------
# STEP 4: Train Models
# -----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
}

results = {}
predictions = {}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    predictions[name] = y_pred


# -----------------------------
# STEP 5: Evaluate Models
# -----------------------------
print("\n--- Accuracy Comparison ---")
for name, acc in results.items():
    print(f"{name}: {acc * 100:.2f}%")

best_model_name = max(results, key=results.get)
print(f"\nBest model: {best_model_name} ({results[best_model_name] * 100:.2f}%)")

print(f"\nDetailed report for {best_model_name}:")
print(classification_report(y_test, predictions[best_model_name], target_names=iris.target_names))


# -----------------------------
# STEP 6: Visualize Confusion Matrix (best model)
# -----------------------------
cm = confusion_matrix(y_test, predictions[best_model_name])
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=iris.target_names, yticklabels=iris.target_names
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title(f"Confusion Matrix - {best_model_name}")
plt.savefig("confusion_matrix.png", dpi=120, bbox_inches="tight")
plt.close()
print("Saved confusion_matrix.png")

print("\nDone! Check iris_pairplot.png and confusion_matrix.png for visuals.")
