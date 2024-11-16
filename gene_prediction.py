import streamlit as st
import joblib
import pandas as pd


# Load the trained model
model = joblib.load('gene_expression_model.pkl')

# Title and description of the app
st.title("Gene Expression Prediction App")
st.write("""
This app predicts the presence of cancer based on gene expression levels.
Enter the values for Gene One and Gene Two below to get the prediction.
""")

# Input fields for user
gene_one = st.number_input("Gene One Expression Level:", min_value=0.0, max_value=100.0, value=5.0)
gene_two = st.number_input("Gene Two Expression Level:", min_value=0.0, max_value=100.0, value=5.0)

# Predict button
if st.button("Predict"):
    # Create a DataFrame for the model
    input_data = pd.DataFrame({
        'Gene One': [gene_one],
        'Gene Two': [gene_two]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display the result
    if prediction == 1:
        st.success("The model predicts that cancer is PRESENT.")
    else:
        st.info("The model predicts that cancer is NOT present.")

