import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("synthetic_customer_churn_100k.csv")

# Clean Column Names
df.columns = df.columns.str.lower().str.strip()

# Convert Churn Column
if df["churn"].dtype == "object":
    df["churn"] = df["churn"].map({"No": 0, "Yes": 1})

# Features and Target
X = df.drop("churn", axis=1)
y = df["churn"]

# One-Hot Encoding
X = pd.get_dummies(X, drop_first=True)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest Model
rf = RandomForestClassifier(
    n_estimators=50,
    max_depth=10,
    random_state=42
)

# Train Model
rf.fit(X_train, y_train)

# Prediction
y_pred = rf.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save Model
joblib.dump(rf, "churn_model.pkl")
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model Saved Successfully!")



