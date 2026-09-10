Python, Data Science, Machine Learning & Deep Learning

Welcome to my **complete Python learning and practice repository**.

This repository contains my journey from **Python programming fundamentals and debugging** to **Data Science, Data Analysis, Visualization, Web Scraping, Machine Learning, and Deep Learning**.

The goal of this repository is to build a strong understanding of Python and its ecosystem through **hands-on practice, implementations, exercises, projects, and real-world examples**.

---

About This Repository

This repository brings together everything I have learned and practiced while working with Python and related technologies.

It starts with the fundamentals of Python and gradually moves toward advanced topics such as:

* Python Programming
* Variables & Data Types
* Operators
* Conditional Statements
* Loops
* Functions
* Strings
* Lists, Tuples, Sets & Dictionaries
* Debugging
* Exception Handling
* Object-Oriented Programming
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Data Analysis
* Data Visualization
* Web Scraping
* Selenium
* Machine Learning
* Machine Learning Algorithms
* Model Evaluation
* Feature Engineering
* Deep Learning
* Neural Networks
* And more

---

Contents

1. [Python Fundamentals](#-python-fundamentals)
2. [Debugging](#-debugging)
3. [NumPy](#-numpy)
4. [Pandas](#-pandas)
5. [Data Visualization](#-data-visualization)
6. [Seaborn](#-seaborn)
7. [Web Scraping](#-web-scraping)
8. [Selenium](#-selenium)
9. [Machine Learning](#-machine-learning)
10. [Machine Learning Algorithms](#-machine-learning-algorithms)
11. [Deep Learning](#-deep-learning)
12. [Tools & Technologies](#-tools--technologies)
13. [Repository Structure](#-repository-structure)
14. [Learning Approach](#-learning-approach)
15. [Future Plans](#-future-plans)

---

Python Fundamentals

The repository begins with the core concepts of Python programming.

### Topics Covered

* Variables
* Data Types
* Type Conversion
* Input & Output
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators
* Conditional Statements
* `if`, `elif`, `else`
* `while` Loops
* `for` Loops
* `break`
* `continue`
* `pass`
* Nested Loops
* Strings
* String Methods
* Lists
* Tuples
* Sets
* Dictionaries
* Functions
* Lambda Functions
* List Comprehension
* Dictionary Comprehension
* Set Comprehension
* Modules
* File Handling
* Exception Handling
* Object-Oriented Programming

The beginner exercises focus on understanding Python syntax and developing problem-solving skills.

---

 Debugging

This section contains Python programs and examples focused on identifying and fixing errors.

Topics Include

* Syntax Errors
* Runtime Errors
* Logical Errors
* Common Python Errors
* Debugging Techniques
* Reading Error Messages
* Using `try` and `except`
* Testing and troubleshooting code

The purpose of this section is to understand not only how to write code, but also how to **find and fix problems in code**.

---

NumPy

NumPy is used for numerical computing and forms an important part of the Python Data Science ecosystem.

Topics Covered

* NumPy Arrays
* Creating Arrays
* Array Dimensions
* Array Indexing
* Array Slicing
* Array Reshaping
* Array Operations
* Mathematical Operations
* Statistical Functions
* Random Numbers
* Array Aggregation
* Broadcasting
* Matrix Operations

Example:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(numbers.mean())
print(numbers.sum())
```

---

# 🐼 Pandas

Pandas is used for data manipulation and analysis.

### Topics Covered

* Series
* DataFrames
* Creating DataFrames
* Reading CSV Files
* Reading Excel Files
* Data Selection
* Filtering Data
* Sorting
* Adding and Removing Columns
* Handling Missing Values
* Data Cleaning
* GroupBy
* Aggregation
* Merging DataFrames
* Joining DataFrames
* Data Transformation

Example:

```python
import pandas as pd

data = pd.read_csv("data.csv")

print(data.head())
print(data.info())
print(data.describe())
```

---

# 📊 Data Visualization

Data visualization is used to understand and communicate information contained in datasets.

### Libraries Used

* Matplotlib
* Seaborn

### Topics Include

* Line Charts
* Bar Charts
* Histograms
* Scatter Plots
* Pie Charts
* Box Plots
* Heatmaps
* Distribution Plots
* Customizing Charts
* Comparing Variables
* Visualizing Relationships

---

Seaborn

Seaborn is used to create statistical visualizations with Python.

### Topics Covered

* `scatterplot()`
* `lineplot()`
* `barplot()`
* `countplot()`
* `histplot()`
* `boxplot()`
* `violinplot()`
* `heatmap()`
* `pairplot()`
* Distribution Analysis
* Correlation Visualization

Example:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df, x="age", y="salary")

plt.show()
```

---

 Web Scraping

This section contains experiments and projects related to collecting data from websites using Python.

### Topics Include

* HTTP Requests
* HTML Structure
* HTML Parsing
* Extracting Text
* Extracting Links
* Extracting Tables
* Data Collection
* Saving Scraped Data
* Working with Dynamic Websites

Libraries and tools include:

* BeautifulSoup
* Requests
* Selenium

---

Selenium

Selenium is used for browser automation and scraping dynamic websites.

### Topics Covered

* Opening Websites
* Finding Web Elements
* CSS Selectors
* XPath
* Clicking Buttons
* Entering Text
* Form Automation
* Page Navigation
* Handling Dynamic Content
* Waiting for Elements
* Extracting Data
* Browser Automation

Example:

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")

print(driver.title)

driver.quit()
```

---

Machine Learning

The Machine Learning section contains implementations and experiments with different Machine Learning techniques.

### Topics Covered

* Introduction to Machine Learning
* Supervised Learning
* Unsupervised Learning
* Classification
* Regression
* Clustering
* Training & Testing Data
* Feature Selection
* Feature Engineering
* Data Preprocessing
* Model Training
* Model Prediction
* Model Evaluation
* Hyperparameter Tuning
* Cross Validation

---

# 🤖 Machine Learning Algorithms

This repository includes implementations and practice with multiple Machine Learning algorithms.

## Regression

* Linear Regression
* Multiple Linear Regression
* Polynomial Regression
* Ridge Regression
* Lasso Regression

## Classification

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Naive Bayes

## Ensemble Learning

* Random Forest
* Gradient Boosting
* AdaBoost
* XGBoost
* Other boosting techniques

## Clustering

* K-Means Clustering
* Hierarchical Clustering
* DBSCAN

## Dimensionality Reduction

* Principal Component Analysis (PCA)

---

Model Evaluation

Different evaluation techniques are used depending on the Machine Learning problem.

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC

### Regression Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

Deep Learning

The Deep Learning section focuses on neural networks and modern AI techniques.

### Topics Include

* Introduction to Neural Networks
* Artificial Neural Networks
* Neurons
* Activation Functions
* Forward Propagation
* Backpropagation
* Loss Functions
* Optimizers
* Training Neural Networks
* Validation
* Overfitting
* Underfitting
* Regularization
* Batch Training
* Epochs
* Model Evaluation

### Deep Learning Concepts

* ANN
* CNN
* RNN
* LSTM
* Neural Network Architecture
* Hyperparameter Tuning

---

# 🛠️ Tools & Technologies

The repository uses a variety of Python libraries and technologies.

### Programming

* Python

### Data Science

* NumPy
* Pandas
* Matplotlib
* Seaborn

### Web Scraping

* Requests
* BeautifulSoup
* Selenium

### Machine Learning

* Scikit-learn
* XGBoost

### Deep Learning

* TensorFlow
* Keras
* PyTorch

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---


---

Learning Approach

This repository follows a practical, step-by-step learning approach.

### 1. Learn the Concept

Understand the basic theory behind a topic.

### 2. Write Code

Implement the concept using Python.

### 3. Practice

Solve exercises and assignment-style problems.

### 4. Debug

Identify and fix errors in the code.

### 5. Apply

Use the concepts in practical examples and projects.

### 6. Build

Combine multiple concepts to create complete projects.

---

# 🚀 Projects

As the repository grows, practical projects will be added to apply the concepts learned throughout the journey.

Possible projects include:

* Data Analysis Projects
* Data Visualization Projects
* Web Scraping Projects
* Machine Learning Prediction Projects
* Classification Projects
* Regression Projects
* Deep Learning Projects
* End-to-End AI Projects

---

# 📌 Current Focus

My current learning path is focused on building strong foundations and gradually moving toward advanced AI and Data Science concepts.

```text
Python
   ↓
Debugging
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
Data Analysis
   ↓
Web Scraping / Selenium
   ↓
Machine Learning
   ↓
Machine Learning Algorithms
   ↓
Deep Learning
   ↓
AI Projects
```

---

# 🔮 Future Plans

I plan to continue expanding this repository with:

* Advanced Python
* Advanced Data Analysis
* More Real-World Datasets
* Advanced Machine Learning
* Feature Engineering
* Model Optimization
* Deep Learning Projects
* Computer Vision
* Natural Language Processing
* Generative AI
* End-to-End AI Projects
* Deployment of Machine Learning Models
* MLOps

---

# 📌 Purpose of This Repository

This repository serves as:

* 📚 A personal learning record
* 💻 A Python practice repository
* 🧠 A Machine Learning knowledge base
* 📊 A Data Science portfolio
* 🤖 An AI development journey
* 🚀 A collection of practical projects

It also allows me to track my progress and revisit concepts whenever needed.

---

# ⭐ Technologies

```text
Python
NumPy
Pandas
Matplotlib
Seaborn
BeautifulSoup
Selenium
Scikit-learn
XGBoost
TensorFlow
Keras
PyTorch
Jupyter Notebook
Git
GitHub
```

---

# 🤝 Contributions

This is primarily a personal learning repository, but suggestions, improvements, and constructive feedback are always welcome.

If you find an issue or have a better approach to a problem, feel free to open an issue or submit a pull request.

---

# 📜 License

This repository is created for **educational and learning purposes**.

---

## 👨‍💻 Author

**Truck**

Learning Python, Data Science, Machine Learning, Deep Learning, and Artificial Intelligence — one concept at a time.

---

⭐ **If you find this repository useful, consider giving it a star!**

```

### One recommendation

Since you're putting **everything from basic Python to Deep Learning** in one repository, I'd name it something broad like:

**`python-data-science-machine-learning`**

or, if you want it to feel more like a personal learning journey:

**`python-to-ai`** ⭐

The second one is much cleaner and memorable for a portfolio.
```
