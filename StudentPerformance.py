# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load dataset (Excel)
data = pd.read_excel("student data.xlsx")

# Handle missing values
data = data.fillna(data.mean())
print("Dataset Preview:\n")
print(data.head())
# Create Pass/Fail column
data['result'] = np.where(data['final_score'] >= 40, 1, 0)
# Features and targets
X = data[['study_hours', 'attendance', 'internal_marks']]
y_reg = data['final_score']
y_clf = data['result']
# Train-Test Split
X_train, X_test, y_reg_train, y_reg_test, y_clf_train, y_clf_test = train_test_split(
    X, y_reg, y_clf, test_size=0.2, random_state=42, stratify=y_clf)
print("\n--- Linear Regression ---")
lr = LinearRegression()
lr.fit(X_train, y_reg_train)
y_pred_reg = lr.predict(X_test)
print("MSE:", mean_squared_error(y_reg_test, y_pred_reg))
print("R2 Score:", r2_score(y_reg_test, y_pred_reg))
X_single = data[['study_hours']]
y_single = data['final_score']
lr_single = LinearRegression()
lr_single.fit(X_single, y_single)
y_line = lr_single.predict(X_single)
plt.figure()
plt.scatter(X_single, y_single)
plt.plot(X_single, y_line)
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Scatter Plot with Regression Line")
plt.show()
print("\n--- Logistic Regression ---")
log_reg = LogisticRegression(max_iter=200, class_weight='balanced')
log_reg.fit(X_train, y_clf_train)
y_pred_clf = log_reg.predict(X_test)
print("Accuracy:", accuracy_score(y_clf_test, y_pred_clf))
print("Confusion Matrix:\n", confusion_matrix(y_clf_test, y_pred_clf))
print("\nClassification Report:\n")
print(classification_report(y_clf_test, y_pred_clf, zero_division=0))
print("\n--- Sample Prediction ---")
sample = pd.DataFrame([[6, 80, 60]],
                      columns=['study_hours', 'attendance', 'internal_marks'])
pred_score = lr.predict(sample)
pred_result = log_reg.predict(sample)
print("Predicted Score:", round(pred_score[0], 2))
if pred_result[0] == 1:
    print("Result: PASS")
else:
    print("Result: FAIL")
