import streamlit as st
import requests
import os

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.title("Bayesian A/B Tester")

metric_type = st.selectbox("Metric type", ["binary", "count", "continuous"])
control_input = st.text_area("Control data (comma separated)")
treatment_input = st.text_area("Treatment data (comma separated)")

if st.button("Analyze"):
    control_data = [float(x) for x in control_input.split(",")]
    treatment_data = [float(x) for x in treatment_input.split(",")]

    payload = {
        "metric_type": metric_type,
        "control_data": control_data,
        "treatment_data": treatment_data
    }
    response = requests.post(f"{API_URL}/analyze", json=payload)
    st.json(response.json())
