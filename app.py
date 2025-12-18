
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

# ==================== CONFIG & STYLING ====================
st.set_page_config(
    page_title="Naira-Sentry Pro",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
        }
        .input-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 12px;
            color: white;
            margin-bottom: 2rem;
        }
        .result-section {
            margin-top: 2rem;
            padding: 2rem;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# ==================== LOAD MODEL ====================


@st.cache_resource
def load_model():
    # Simple path for root-level app.py
    model_path = os.path.join(os.getcwd(), "models",
                              "isolation_forest_model.pkl")

    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}")
        st.stop()

    return joblib.load(model_path)


model = load_model()

# ==================== DATA CATEGORIES ====================
locations = ['Aba', 'Abuja', 'Benin City', 'Enugu', 'Ibadan',
             'Kaduna', 'Kano', 'Lagos', 'Onitsha', 'Port Harcourt']
channels = ['Bank Transfer', 'Card', 'Mobile App', 'USSD']
txn_types = ['deposit', 'payment', 'transfer', 'withdrawal']
devices = ['atm', 'mobile', 'pos', 'web']

# ==================== PAGE HEADER ====================
col_title = st.columns([1])
with col_title[0]:
    st.markdown("""
        <div class="title-container">
            <h1>🔒 Naira-Sentry Pro</h1>
            <p style="font-size: 1.1rem; color: #666;">
                Advanced Fraud Detection for Nigerian Transactions
            </p>
        </div>
    """, unsafe_allow_html=True)


# ==================== INPUT SECTION ====================
st.markdown("### 📝 Enter Transaction Details")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**💰 Transaction Details**")
    amount = st.number_input(
        "Amount (₦)",
        min_value=1,
        value=5000,
        help="Transaction amount in Nigerian Naira"
    )
    hour = st.slider(
        "Hour (24h)",
        min_value=0,
        max_value=23,
        value=12,
        help="Time of transaction in 24-hour format"
    )

with col2:
    st.markdown("**🌍 Location & Channel**")
    location = st.selectbox(
        "Location",
        locations,
        help="Transaction location"
    )
    channel = st.selectbox(
        "Payment Channel",
        channels,
        help="Method used for transaction"
    )

with col3:
    st.markdown("**📱 Device & Day**")
    device = st.selectbox(
        "Device Used",
        devices,
        help="Device type used for transaction"
    )
    day = st.slider(
        "Day of Week",
        min_value=0,
        max_value=6,
        value=2,
        help="0=Monday, 6=Sunday"
    )
    txn_type = st.selectbox(
        "Transaction Type",
        txn_types,
        help="Type of transaction"
    )

st.markdown("---")

# ==================== PREDICTION LOGIC ====================
col_button = st.columns([1, 4, 1])
with col_button[1]:
    verify_button = st.button(
        "🔍 Verify Transaction",
        use_container_width=False,
        type="primary"
    )

if verify_button:
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

    # ==================== RESULT DISPLAY ====================
    st.markdown("---")

    if prediction == -1:
        st.markdown("""
            <div style="background-color: #fee; border-left: 4px solid #c33; padding: 20px; border-radius: 8px;">
                <h2 style="color: #c33; margin-top: 0;">⚠️ FRAUD ALERT</h2>
                <p style="font-size: 1.1rem; color: #333;">
                    Suspicious activity detected in this transaction
                </p>
                <p style="color: #666;">
                    <strong>Anomaly Score:</strong> {:.4f}
                </p>
            </div>
        """.format(abs(score)), unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background-color: #efe; border-left: 4px solid #3a3; padding: 20px; border-radius: 8px;">
                <h2 style="color: #3a3; margin-top: 0;">✅ TRANSACTION VERIFIED</h2>
                <p style="font-size: 1.1rem; color: #333;">
                    No fraudulent activity detected
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

    # Display transaction summary
    st.markdown("### 📊 Transaction Summary")
    summary_df = pd.DataFrame([{
        "Amount": f"₦{amount:,}",
        "Location": location,
        "Channel": channel,
        "Device": device.capitalize(),
        "Type": txn_type.capitalize(),
        "Time": f"{hour:02d}:00",
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
    }])
    st.dataframe(summary_df, hide_index=True)
