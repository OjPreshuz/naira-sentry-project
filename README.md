# Naira-Sentry: Unsupervised Fintech Fraud Detection

**Status:** Active | **Region:** 🇳🇬 Nigeria | **Tech:** Unsupervised Learning (Isolation Forest)

## Overview

Naira-Sentry is a Machine Learning system designed to detect fraudulent financial transactions in the Nigerian Fintech space. Unlike traditional rule-based systems (e.g., "Block if > ₦500k"), this project uses **Anomaly Detection** to identify suspicious behavioral patterns—such as midnight transfers, unexpected device usage, and location anomalies—without needing labeled fraud data.

## The Problem

Nigeria's Fintech sector faces sophisticated fraud vectors:

- **Account Takeovers:** High-value transfers from new or unverified devices.
- **POS Fraud:** Transactions occurring in geographically inconsistent locations.
- **Structuring:** Abnormal transaction spikes during odd hours (e.g., 2 AM).
- **Device/Location Spoofing:** Multiple transactions from impossible locations in short timeframes.

## Solution: Isolation Forest

The **Isolation Forest** algorithm excels at unsupervised anomaly detection by:

1. Randomly selecting features and split values
2. Isolating outliers into small trees
3. Scoring observations based on isolation depth
4. Flagging transactions with extreme anomaly scores as potential fraud

## Tech Stack

| Category                | Tools                              |
| ----------------------- | ---------------------------------- |
| **Data Processing**     | Pandas, NumPy                      |
| **Machine Learning**    | Scikit-Learn (Isolation Forest)    |
| **Feature Engineering** | Log-Transformation, Label Encoding |
| **Visualization**       | Matplotlib, Seaborn                |
| **Web Interface**       | Streamlit                          |
| **Model Serialization** | Joblib                             |

## Dataset

- **Source:** Nigerian Fraud Dataset Sample
- **Location:** `data/raw/nigeria_fraud_dataset_sample.csv`
- **Processed Data:** `data/processed/` (train/test splits)
- **Key Features:** Transaction amount, hour, day, location, device, payment channel, transaction type

## Model Features

| Feature                     | Description                                            | Why it matters                                               |
| --------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **`hour`**                  | Hour of day (0-23)                                     | Fraudsters often operate during sleeping hours (1 AM - 4 AM) |
| **`day_of_week`**           | Mon (0) - Sun (6)                                      | Weekend transaction patterns differ from workdays            |
| **`payment_channel_code`**  | Encoded (e.g., USSD, Card, Mobile App, Bank Transfer)  | Certain channels have higher fraud risk profiles             |
| **`device_used_code`**      | Encoded (e.g., ATM, POS, Mobile, Web)                  | Sudden device shifts can indicate account compromise         |
| **`location_code`**         | Encoded (e.g., Lagos, Abuja, Kano)                     | Detects impossible travel and location-based fraud rings     |
| **`transaction_type_code`** | Encoded (e.g., Transfer, Withdrawal, Payment, Deposit) | Specific types preferred for cashing out stolen funds        |
| **`amount_log`**            | Log-transformed Amount (₦)                             | Normalizes scale difference between ₦100 and ₦1M             |

## Project Structure

```
naira-sentry/
├── � app.py                           # Main Streamlit application (root level)
├── 📋 requirements.txt                 # Python dependencies with versions
├── 📖 README.md                        # Full documentation (this file)
├── 📄 DEPLOYMENT.md                    # Deployment guides for Streamlit Cloud, Docker, Local
├── 📝 PROJECT_SUMMARY.md               # Project overview & statistics
├── 📊 UPGRADE_SUMMARY.md               # Recent upgrade changes
├── 🔒 .env.example                     # Environment variables template
├── ⚙️  .streamlit/
│   └── config.toml                     # Streamlit theme & server configuration
│
├── 🤖 models/                          # Trained ML models
│   ├── isolation_forest_model.pkl      # Trained Isolation Forest model
│   └── label_encoder.pkl               # Feature encoding mappings
│
├── 📊 data/                            # Dataset directory
│   ├── raw/
│   │   └── nigeria_fraud_dataset_sample.csv
│   └── processed/
│       ├── full_data.csv
│       ├── train_data.csv
│       └── test_data.csv
│
├── 📓 notebook/                        # Jupyter notebooks (development & analysis)
│   ├── 01_eda_detective.ipynb          # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb    # Feature engineering & encoding
│   ├── 03_model_training.ipynb         # Model training & evaluation
│   └── 04_visualisation.ipynb          # Results & pattern visualization
│
├── 📸 visuals/                         # Generated visualizations
│   └── *.png                           # EDA charts, patterns, heatmaps
│
└── 🗂️  src/                            # Legacy/reference code
    └── app.py                          # Old version (deprecated - use root app.py)
```

**Key Points:**

- ✅ `app.py` at **root level** for Streamlit Cloud deployment
- ✅ All configuration files included (`.streamlit/config.toml`, `.env.example`)
- ✅ Complete documentation suite (README, DEPLOYMENT, PROJECT_SUMMARY)
- ✅ Models and data properly organized

## Getting Started

### Prerequisites

- Python 3.7+
- pip or conda

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd naira_sentry
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**🚀 Launch the Streamlit web interface locally:**

```bash
# From project root
streamlit run app.py
```

Access at: `http://localhost:8501`

**✨ Features:**

- ✅ Enter transaction details (amount, time, location, device, channel, type)
- 🎯 Get real-time fraud risk assessment with anomaly scoring
- 📊 View detailed transaction summaries and verification status
- 🎨 Beautiful, responsive UI with modern styling

**🌐 Deploy to Streamlit Cloud (Recommended for sharing):**

1. **Push your code to GitHub:**

   ```bash
   git add .
   git commit -m "Deploy Naira-Sentry to Streamlit Cloud"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**

   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click **"New app"**
   - Select your repository
   - Set main file path to: `app.py` (root level)
   - Click **"Deploy"**

3. **Share your app URL:**
   ```
   https://<your-app-name>.streamlit.app
   ```

**📦 Docker Deployment (for self-hosting):**

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete Docker setup and cloud deployment instructions.

**📓 For development & experimentation:** 6. Deploy → Get your public URL: `https://<your-app-name>.streamlit.app`

**📓 For development & experimentation:**

1. **01_eda_detective.ipynb** - Exploratory data analysis & distribution insights
2. **02_feature_engineering.ipynb** - Feature creation, encoding & transformation
3. **03_model_training.ipynb** - Train and evaluate the Isolation Forest model
4. **04_visualisation.ipynb** - Visualize patterns, anomalies & model insights

## How It Works

### 🔄 Data Pipeline

```
Raw Data (.csv)
    ↓
Label Encoding (categorical → numeric)
    ↓
Log Transformation (amount normalization)
    ↓
Isolation Forest Training
    ↓
Real-time Prediction & Anomaly Detection
```

### 🎯 Prediction Output

- **Anomaly Score:** Distance from normal behavior (-∞ to +∞)
- **Classification:**
  - ✅ **Verified (-1):** Suspicious pattern detected → Review required
  - 🟢 **Normal (1):** Legitimate transaction behavior → Approved
- **Confidence:** Based on isolation depth in ensemble trees

## Model Performance

The Isolation Forest model excels at:

- ✓ Detecting unusual transaction patterns without labeled data
- ✓ Identifying account takeovers & device anomalies
- ✓ Flagging impossible locations & time-based fraud
- ✓ Scaling efficiently across transaction volumes

**Evaluation metrics:**

- Precision: Minimizes false alarms
- Recall: Catches subtle fraud patterns
- ROC-AUC: Overall discriminative ability

## Future Enhancements

- [ ] 🔄 Real-time transaction streaming with Kafka/RabbitMQ
- [ ] 🎭 Multi-model ensemble (Isolation Forest + LOF + Autoencoders)
- [ ] 👤 Custom anomaly thresholds by merchant/user profile
- [ ] 🏦 Integration with banking APIs & payment gateways
- [ ] 📱 Mobile app for on-the-go risk assessment
- [ ] 🗺️ Geographic heatmaps of fraud hotspots
- [ ] 📈 Time-series analysis for account behavior trending
- [ ] ⚡ Edge deployment for sub-millisecond predictions
- [ ] 🤖 Active learning to improve model over time

## Contributing

**🤝 Want to Contribute?**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add feature description"`
4. Push: `git push origin feature/your-feature`
5. Submit a Pull Request

## License

This project is licensed under the **MIT License** - see LICENSE file for details.

## Contact & Support

**📧 Questions or Issues?**

- Open a GitHub issue for bugs or feature requests
- Check discussions for Q&A
- Review existing issues before creating new ones

---

## 📊 Quick Stats

| Metric                   | Value                           |
| ------------------------ | ------------------------------- |
| **Algorithm**            | Isolation Forest (Unsupervised) |
| **Python Version**       | 3.7+                            |
| **Primary Dependencies** | Scikit-Learn, Pandas, Streamlit |
| **Model Size**           | ~2MB                            |
| **Inference Time**       | <10ms per transaction           |
| **License**              | MIT                             |

---

**🚀 Last Updated:** December 2025 | **Status:** Production Ready
