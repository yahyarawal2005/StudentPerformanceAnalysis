📊 Student Performance Prediction System

A Machine Learning project that predicts student final scores and pass/fail outcomes based on academic inputs like study hours, attendance, and internal marks.

🚀 Overview

This project applies both regression and classification techniques:

Linear Regression → Predicts final exam score
Logistic Regression → Predicts pass/fail result

It also includes data preprocessing, model evaluation, and visualization.

📁 Dataset

The dataset is loaded from an Excel file:

student data.xlsx
Features used:
study_hours
attendance
internal_marks
Target variables:
final_score (for regression)
result (generated: Pass = 1, Fail = 0)
⚙️ Workflow
1. Data Preprocessing
Missing values handled using mean imputation

New column result created:

result = 1 if final_score >= 40 else 0
2. Train-Test Split
80% training, 20% testing
Stratified split used for classification balance
3. Models Used
🔹 Linear Regression
Predicts continuous values (final score)
Evaluation metrics:
Mean Squared Error (MSE)
R² Score
🔹 Logistic Regression
Predicts binary outcome (Pass/Fail)
Evaluation metrics:
Accuracy
Confusion Matrix
Classification Report
📈 Visualization
Scatter plot of Study Hours vs Final Score
Regression line to show trend
🔮 Sample Prediction

Example input:

Study Hours: 6  
Attendance: 80  
Internal Marks: 60  

Output:

Predicted Score: XX  
Result: PASS / FAIL  
🛠️ Tech Stack
Python
Pandas
NumPy
Matplotlib
Scikit-learn
▶️ How to Run
Clone the repository
git clone https://github.com/your-username/student-performance-ml.git
Install dependencies
pip install pandas numpy matplotlib scikit-learn openpyxl
Add dataset file:
student data.xlsx
Run the script
python main.py
📊 Results
Regression model provides numerical score prediction
Classification model determines pass/fail status
Balanced logistic regression handles class imbalance
⚠️ Limitations (Don’t ignore this)
Uses a small/basic dataset
Only linear relationships are modeled
No hyperparameter tuning
No cross-validation
🔥 Future Improvements (What actually matters)
Add advanced models (Random Forest, XGBoost)
Perform feature engineering
Use cross-validation for reliability
Deploy as a web app (Flask / Streamlit)
Add real-world dataset
📌 Conclusion

This project demonstrates the fundamentals of supervised learning, combining regression and classification to analyze student performance.
