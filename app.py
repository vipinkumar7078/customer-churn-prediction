
import streamlit as st
import pandas as pd
import joblib

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------
# LOAD MODEL
# --------------------
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# --------------------
# CUSTOM CSS
# --------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.metric-card {
    background-color:#1f2937;
    padding:15px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

# --------------------
# HEADER
# --------------------
st.title("📊 Customer Churn Prediction Dashboard")
st.caption("AI Powered Customer Retention Analytics")

# --------------------
# SIDEBAR
# --------------------
st.sidebar.header("Customer Information")

customerid = st.sidebar.number_input(
    "Customer ID",
    min_value=1,
    value=1001
)

age = st.sidebar.slider(
    "Age",
    18,
    80,
    30
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    100,
    12
)

monthlycharges = st.sidebar.number_input(
    "Monthly Charges",
    value=500.0
)

totalcharges = st.sidebar.number_input(
    "Total Charges",
    value=5000.0
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female","Male","Other"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

paymentmethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Bank transfer",
        "Credit card",
        "Electronic check",
        "Mailed check"
    ]
)

# --------------------
# KPI CARDS
# --------------------
c1,c2,c3,c4 = st.columns(4)

c1.metric("Age", age)
c2.metric("Tenure", tenure)
c3.metric("Monthly Charges", f"₹{monthlycharges}")
c4.metric("Total Charges", f"₹{totalcharges}")

# --------------------
# PREDICTION
# --------------------
if st.button("🔍 Predict Churn"):

    data = {
        'customerid':[customerid],
        'age':[age],
        'tenure':[tenure],
        'monthlycharges':[monthlycharges],
        'totalcharges':[totalcharges],
        'gender_Male':[1 if gender=="Male" else 0],
        'gender_Other':[1 if gender=="Other" else 0],
        'contract_One year':[1 if contract=="One year" else 0],
        'contract_Two year':[1 if contract=="Two year" else 0],
        'paymentmethod_Credit card':[1 if paymentmethod=="Credit card" else 0],
        'paymentmethod_Electronic check':[1 if paymentmethod=="Electronic check" else 0],
        'paymentmethod_Mailed check':[1 if paymentmethod=="Mailed check" else 0]
    }

    input_df = pd.DataFrame(data)

    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_columns]

    prediction = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_df)[0][1]
    else:
        probability = 0.5

    st.divider()

    st.subheader("Prediction Result")

    st.progress(float(probability))

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    if probability < 0.30:
        st.success("🟢 LOW RISK CUSTOMER")
    elif probability < 0.70:
        st.warning("🟡 MEDIUM RISK CUSTOMER")
    else:
        st.error("🔴 HIGH RISK CUSTOMER")

    st.subheader("Customer Summary")

    st.dataframe(input_df)

    report = input_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="customer_report.csv",
        mime="text/csv"
    )

st.divider()

# st.markdown("""
# ### 🚀 Project Tech Stack

# - Machine Learning: Random Forest
# - Frontend: Streamlit
# - Data Processing: Pandas
# - Model Storage: Joblib
# - Purpose: Customer Churn Prediction
# """)
