# 🚀 Customer Churn Prediction Using Machine Learning

## 📌 Project Overview

Customer Churn Prediction is a Machine Learning project that predicts whether a customer is likely to leave a company's service based on customer demographics, subscription details, and billing information.

The project uses multiple machine learning algorithms and deploys the best-performing model through an interactive Streamlit dashboard.

---

## 🎯 Objectives

* Identify customers at risk of churn.
* Improve customer retention strategies.
* Analyze factors affecting customer behavior.
* Provide real-time churn prediction through a user-friendly dashboard.

---

## 📊 Dataset Features

| Feature        | Description                  |
| -------------- | ---------------------------- |
| CustomerID     | Unique Customer Identifier   |
| Age            | Customer Age                 |
| Gender         | Customer Gender              |
| Tenure         | Duration of Service          |
| MonthlyCharges | Monthly Subscription Charges |
| TotalCharges   | Total Amount Paid            |
| Contract       | Contract Type                |
| PaymentMethod  | Payment Method               |
| Churn          | Target Variable              |

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

### Development Tools

* Google Colab
* Visual Studio Code
* GitHub

---

## 🤖 Machine Learning Models

The following models were implemented:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Best Model

Random Forest Classifier achieved the highest performance and was selected for deployment.

---

## 📈 Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC Curve

---

## 🏗️ Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── train_model.py
├── Customer_Churn_Prediction.ipynb
├── requirements.txt
├── README.md
├── model_columns.pkl
├── synthetic_customer_churn_100k.csv
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vipinkumar7078/customer-churn-prediction.git
```

Move into the project folder:

```bash
cd customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Dashboard Features

* Customer Information Form
* Churn Prediction
* Risk Analysis
* Customer Summary
* Feature Importance Visualization
* Interactive Dashboard

---

## 📷 Screenshots

Add dashboard screenshots inside the screenshots folder.

Example:

* Dashboard Home
* Prediction Output
* Feature Importance Chart

---

## 🔮 Future Enhancements

* Real-time API Integration
* Cloud Deployment
* Deep Learning Models
* Automated Retention Recommendations
* Advanced Analytics Dashboard

---

## 👨‍💻 Author

**Vipin Kumar**

MCA (Data Analytics Specialization)

Galgotias University

---

## 📄 License

This project is developed for academic and educational purposes.
