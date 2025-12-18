
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# LOAD MODEL
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "models",
                          "isolation_forest_model.pkl")


@st.cache_resource
def load_model():
    return joblib.load(model_path)


model = load_model()

# DEFINE CATEGORIES (Must be in alphabetical order as trained)
locations = ['Aba', 'Abuja', 'Benin City', 'Enugu', 'Ibadan',
             'Kaduna', 'Kano', 'Lagos', 'Onitsha', 'Port Harcourt']
channels = ['Bank Transfer', 'Card', 'Mobile App', 'USSD']
txn_types = ['deposit', 'payment', 'transfer', 'withdrawal']
devices = ['atm', 'mobile', 'pos', 'web']

st.title("Naira-Sentry: Pro Version")
st.markdown("Enter transaction details below to check for fraud.")

# UI LAYOUT
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount (₦)", min_value=1, value=5000)
    hour = st.slider("Hour of Day (24h)", 0, 23, 12)
    location = st.selectbox("Location", locations)
    channel = st.selectbox("Payment Channel", channels)

with col2:
    txn_type = st.selectbox("Transaction Type", txn_types)
    device = st.selectbox("Device Used", devices)
    day = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

# PREDICTION LOGIC
if st.button("Verify Transaction"):
    loc_code = locations.index(location)
    chan_code = channels.index(channel)
    type_code = txn_types.index(txn_type)
    dev_code = devices.index(device)

    # Prepare the input row
    input_df = pd.DataFrame([{
        'hour': hour,
        'day_of_week': day,
        'payment_channel_code': chan_code,
        'device_used_code': dev_code,
        'location_code': loc_code,
        'transaction_type_code': type_code,
        'amount_log': np.log1p(amount)
    }])

    # Get results
    prediction = model.predict(input_df)[0]
    score = model.decision_function(input_df)[0]

    st.markdown("---")
    if prediction == -1:
        st.error(
            "ALERT: Suspicious Transaction Detected")
    else:
        st.success("Transaction Verified")
        st.balloons()
