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
naira_sentry/
├── data/                          # Dataset directory (Git-ignored)
│   ├── raw/
│   │   └── nigeria_fraud_dataset_sample.csv
│   └── processed/
│       ├── full_data.csv
│       ├── train_data.csv
│       └── test_data.csv
├── models/                        # Trained ML models
│   ├── isolation_forest_model.pkl
│   └── label_encoder.pkl
├── notebook/                      # Jupyter notebooks
│   ├── 01_eda_detective.ipynb     # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb # Feature encoding & transformation
│   ├── 03_model_training.ipynb    # Model training & evaluation
│   └── 04_visualisation.ipynb     # Results visualization
├── src/
│   └── app.py                     # Streamlit web application
├── visuals/                       # Generated visualizations
│   ├── amount_distribution.png
│   ├── fraud_cluster.png
│   ├── transaction_frequency.png
│   └── transformed_amount.png
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

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

**Launch the Streamlit web interface:**

```bash
streamlit run src/app.py
```

The application will open at `http://localhost:8501` where you can:

- Enter transaction details (amount, time, location, device, channel, type)
- Get real-time fraud risk assessment
- View detailed transaction analysis

### Notebook Workflow

For development and experimentation:

1. **01_eda_detective.ipynb** - Start here for data exploration
2. **02_feature_engineering.ipynb** - Feature creation and transformation
3. **03_model_training.ipynb** - Train and evaluate the Isolation Forest model
4. **04_visualisation.ipynb** - Visualize patterns and anomalies

## How It Works

### Data Pipeline

1. **Raw Data** → Loaded from CSV
2. **Label Encoding** → Categorical features (location, channel, device, type) converted to integers
3. **Log Transformation** → Transaction amounts normalized to log scale
4. **Model Training** → Isolation Forest trained on engineered features
5. **Prediction** → New transactions scored for anomaly likelihood

### Prediction Output

- **Anomaly Score:** -1 (anomaly/fraud) or 1 (normal)
- **Decision:** Transactions flagged for review or approved
- **Confidence:** Based on isolation depth in ensemble trees

## Model Performance

The model is evaluated on:

- Detection of unusual transaction patterns
- Minimal false positives for legitimate transactions
- Robustness across different transaction magnitudes and times

## Future Enhancements

- [ ] Real-time transaction streaming with Kafka
- [ ] Multi-model ensemble (Isolation Forest + Local Outlier Factor)
- [ ] Custom anomaly thresholds by merchant/user profile
- [ ] Integration with banking APIs
- [ ] Mobile app for on-the-go risk assessment
- [ ] Geographic heatmaps of fraud hotspots
- [ ] Time-series analysis for account behavior trending

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contact & Support

For questions or issues, please open a GitHub issue or contact the development team.

---

**Last Updated:** December 2025
