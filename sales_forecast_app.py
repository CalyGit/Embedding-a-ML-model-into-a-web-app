# Import libraries
import gradio as gr
import pandas as pd
import joblib
from datetime import datetime

# Load the ARIMA model
arima_model = joblib.load('best_model.pkl')

def sales_forecast(date, store_nbr, onpromotion, year, cluster, dcoilwtico):
    # Parse the date input into a datetime object
    date = datetime.strptime(date, "%Y-%m-%d")

    # Create a DataFrame with the user inputs
    user_input = pd.DataFrame({
        'Date': [date],
        'Store Number': [store_nbr],
        'On promotion': [onpromotion],
        'Year': [year],
        'Cluster': [cluster],
        'Daily Oil Price': [dcoilwtico]
    })

    # Make the sales forecast prediction using the ARIMA model
    forecast = arima_model.forecast(steps=1)  
    return forecast[0]  # Return the forecasted value


# Create the interface
iface = gr.Interface(
    fn=sales_forecast,
    inputs=[
        gr.inputs.Textbox(label="Date"),
        gr.inputs.Number(label="Store Number"),
        gr.inputs.Number(label="On promotion"),
        gr.inputs.Number(label="Year"),
        gr.inputs.Number(label="Cluster"),
        gr.inputs.Number(label="Daily Oil Price")
    ],
    outputs=gr.outputs.Textbox(),

title="<div style='text-align: center;'>"
          "<span style='font-family: \"Times New Roman\", sans-serif; font-style: italic; font-weight: bold;'>CORPORATION FAVORITA</span>"
          "<p style='font-size: 16px;'>Predict sales across our different stores</p>"
          "</div>",
theme="light"  # Set the theme to "light"
)

if __name__ == "__main__":
    iface.launch()





