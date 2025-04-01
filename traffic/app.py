import streamlit as st
import joblib
import numpy as np

# Load the trained model
rfc = joblib.load('model.joblib')

st.title("Machine Predictive Maintenance")

# User Input
col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
    type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    selected_type = type_mapping[selected_type]

with col2:
    air_temperature = st.text_input('Air temperature [K]', value="0")

with col1:
    process_temperature = st.text_input('Process temperature [K]', value="0")

with col2:
    rotational_speed = st.text_input('Rotational speed [rpm]', value="0")

with col1:
    torque = st.text_input('Torque [Nm]', value="0")

with col2:
    tool_wear = st.text_input('Tool wear [min]', value="0")

# Convert inputs to proper numerical format
try:
    air_temperature = float(air_temperature)
    process_temperature = float(process_temperature)
    rotational_speed = float(rotational_speed)
    torque = float(torque)
    tool_wear = float(tool_wear)
except ValueError:
    st.error("Please enter valid numerical values.")
    st.stop()  # Stop execution if conversion fails

# Prediction Logic
failure_pred = ""

if st.button('Predict Failure'):
    input_data = np.array([[selected_type, air_temperature, 
                             process_temperature, rotational_speed,
                             torque, tool_wear]])

    # Make prediction
    failure_pred = rfc.predict(input_data)

    # Display result
    if failure_pred[0] == 1:
        st.error("⚠️ Machine will suffer Failure")
    else:
        st.success("✅ Machine Will Not suffer Failure")
