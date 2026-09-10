import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
url='credit_record.csv'
df = pd.read_csv(url)
df = df.dropna(subset=['STATUS'])

# Practice ke liye sirf 10k rows
df = df.sample(10000, random_state=42)

le = LabelEncoder()
df['STATUS_encoded'] = le.fit_transform(df['STATUS'])

X = df[['ID', 'MONTHS_BALANCE']]
y = df['STATUS_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_classifier = RandomForestClassifier(
    n_estimators=10,
    random_state=42,
    n_jobs=-1
)

rf_classifier.fit(X_train, y_train)


y_pred=rf_classifier.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
classification_rep=classification_report(y_test,y_pred)

print(f"accuracy:, {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)

