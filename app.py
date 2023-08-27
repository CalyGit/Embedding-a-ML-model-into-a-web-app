import streamlit as st
import joblib
import pandas as pd

# Load the trained model
pipeline = joblib.load('churn_prediction_model.pkl')

# Set the background color to white
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Create the Streamlit app
def main():
    # Set the background color of the sidebar
    st.sidebar.markdown(
        """
        <style>
        .sidebar {
            background-color: darkblue;
            color: white;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add image of the company logo
    logo_image = "logo-cf-footer.png"  # Replace with your image filename
    st.image(logo_image, use_column_width=True)

    
    # Create a side widget for app purpose
    st.sidebar.title("Churn Prediction App")
    st.sidebar.write("Welcome to the Churn Prediction App! This app is designed to help you predict customer churn using a machine learning model. Here's how to use the app:")
    
    st.sidebar.subheader("Step 1: Input Customer Information")
    st.sidebar.write("Use the input widgets on the left to provide customer information, including tenure, monthly charges, total charges, and more. Select options for relevant features using checkboxes and dropdowns.")
    
    st.sidebar.subheader("Step 2: Predict Customer Churn")
    st.sidebar.write("Once you've input all the necessary information, click the 'Predict' button below the input widgets. The app will use its machine learning model to predict whether the customer is likely to churn or stay.")
    
    st.sidebar.subheader("Step 3: Interpret Results")
    st.sidebar.write("After clicking the 'Predict' button, the app will display the prediction result. If the prediction indicates that the customer is likely to stay, the app will show 'Customer is likely to stay.' If the prediction indicates churn, the app will show 'Customer is likely to churn.'")
    
    st.sidebar.subheader("Step 4: Explore Further")
    st.sidebar.write("Feel free to adjust the input values and options to see how different factors impact the prediction outcome. The app is designed to assist you in understanding and analyzing customer churn.")
    
    st.sidebar.subheader("About the App")
    st.sidebar.write("This app is powered by a machine learning model that has been trained on customer data to predict churn. It's intended for educational and demonstration purposes. For any questions or assistance, please reach out to our team.")
    
    # Create input widgets for user input
    st.markdown("<h1 style='font-family: Times New Roman, Times, serif; font-size:48px; font-style:italic;'>Customer Churn Prediction</h1>", unsafe_allow_html=True)
    # Create input widgets for user input
    tenure = st.slider("Tenure", 1, 72, 36)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1500.0)
    
    # Create a DataFrame with user input
    user_data = pd.DataFrame({
        'SeniorCitizen_1': [1 if st.checkbox("Senior Citizen") else 0],
        'Partner_Yes': [1 if st.checkbox("Partner") else 0],
        'Dependents_Yes': [1 if st.checkbox("Dependents") else 0],
        'PhoneService_Yes': [1 if st.checkbox("Phone Service") else 0],
        'MultipleLines_No phone service': [0],  # Assuming this is a checkbox
        'MultipleLines_Yes': [1 if st.checkbox("Multiple Lines") else 0],
        'InternetService_Fiber optic': [1 if st.checkbox("Fiber Optic Internet") else 0],
        'InternetService_No': [0],  # Assuming this is a checkbox
        'OnlineSecurity_Yes': [1 if st.checkbox("Online Security") else 0],
        'OnlineBackup_Yes': [1 if st.checkbox("Online Backup") else 0],
        'DeviceProtection_Yes': [1 if st.checkbox("Device Protection") else 0],
        'TechSupport_Yes': [1 if st.checkbox("Tech Support") else 0],
        'StreamingTV_Yes': [1 if st.checkbox("Streaming TV") else 0],
        'StreamingMovies_Yes': [1 if st.checkbox("Streaming Movies") else 0],
        'Contract_One year': [1 if st.checkbox("One Year Contract") else 0],
        'Contract_Two year': [1 if st.checkbox("Two Year Contract") else 0],
        'PaperlessBilling_Yes': [1 if st.checkbox("Paperless Billing") else 0],
        'PaymentMethod_Credit card (automatic)': [0],  # Assuming this is a checkbox
        'PaymentMethod_Electronic check': [1 if st.checkbox("Electronic Check") else 0],
        'PaymentMethod_Mailed check': [1 if st.checkbox("Mailed Check") else 0],
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })
    
    # Create "Predict" button
    predict_button = st.button("Predict")
    
    # Perform prediction when the button is clicked
    if predict_button:
        # Display user input
        st.write("User Input:")
        st.dataframe(user_data)
        
        # Make prediction
        prediction = pipeline.predict(user_data)
        
        # Display prediction result
        if prediction[0] == 0:
            st.write("Prediction: Customer is likely to stay.")
        else:
            st.write("Prediction: Customer is likely to churn.")

if __name__ == "__main__":
    main()

