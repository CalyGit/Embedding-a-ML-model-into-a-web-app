import streamlit as st
import pandas as pd
import numpy as np

# Function for feature processing
def preprocess_data(customer_data):
    # Our preprocessing code here
    # Since we're not using the actual model, we can skip this step in the demo

    # For the demo, we'll return a random prediction (0 or 1) 
    return np.random.randint(2)

# Streamlit app
def main():
    st.title("Customer Churn Prediction App (Demo)")

    # Collect customer attributes from the user
    customer_data = {}
    customer_data['gender'] = st.radio("Gender", ["Male", "Female"])
    customer_data['SeniorCitizen'] = st.selectbox("Senior Citizen", ["0", "1"])
    customer_data['Partner'] = st.selectbox("Partner", ["Yes", "No"])
    customer_data['Dependents'] = st.selectbox("Dependents", ["Yes", "No"])
    customer_data['tenure'] = st.number_input("Tenure", min_value=0, max_value=100, value=30)
    customer_data['PhoneService'] = st.selectbox("Phone Service", ["Yes", "No"])
    customer_data['MultipleLines'] = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    customer_data['InternetService'] = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    customer_data['OnlineSecurity'] = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    customer_data['OnlineBackup'] = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    customer_data['DeviceProtection'] = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    customer_data['TechSupport'] = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    customer_data['StreamingTV'] = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    customer_data['StreamingMovies'] = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    customer_data['Contract'] = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    customer_data['PaperlessBilling'] = st.selectbox("Paperless Billing", ["Yes", "No"])
    customer_data['PaymentMethod'] = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    customer_data['MonthlyCharges'] = st.number_input("Monthly Charges", min_value=0, value=70)
    customer_data['TotalCharges'] = st.number_input("Total Charges", min_value=0, value=2000)

    # Show the entered data in a DataFrame
    st.subheader("Entered Data:")
    data = pd.DataFrame(customer_data, index=[0])
    st.write(data)

    # Preprocess the data (in the actual app, this step will be used to prepare data for model prediction)
    # For the demo, we'll generate a random prediction (0 or 1) based on user inputs
    prediction = preprocess_data(customer_data)

    # Display the prediction when the "Predict" button is clicked
    if st.button("Predict"):
        st.subheader("Prediction")
        if prediction == 1:
            st.write("The customer is likely to churn.")
        else:
            st.write("The customer is not likely to churn.")
if __name__ == "__main__":
    main()
