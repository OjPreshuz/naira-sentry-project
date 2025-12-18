# Data Directory

## Overview

This directory contains raw and processed datasets for the Naira-Sentry fraud detection project.

```
data/
├── raw/                    # Original unprocessed datasets
│   └── nigeria_fraud_dataset_sample.csv
└── processed/              # Cleaned and feature-engineered data
    ├── full_data.csv       # Complete processed dataset
    ├── train_data.csv      # Training subset
    └── test_data.csv       # Testing subset
```

## Obtaining the Data

### Option 1: Download Sample Data

The sample dataset is included in this repository's `raw/` folder:

- `nigeria_fraud_dataset_sample.csv` - Nigerian fintech transaction dataset with fraud labels

### Option 2: Generate Your Own Data

If you have your own transaction data, place it in `raw/` folder with the following columns:

- `amount` - Transaction amount in Nigerian Naira (₦)
- `hour` - Hour of transaction (0-23)
- `day_of_week` - Day of week (0=Monday, 6=Sunday)
- `location` - Transaction location (e.g., Lagos, Abuja, Kano)
- `payment_channel` - Channel used (USSD, Card, Mobile App, Bank Transfer)
- `device_used` - Device type (ATM, POS, Mobile, Web)
- `transaction_type` - Type of transaction (Transfer, Withdrawal, Payment, Deposit)

## Data Processing

To process raw data into features:

1. **Navigate to notebooks directory:**

   ```bash
   cd notebooks
   ```

2. **Run the EDA notebook** (exploratory data analysis):

   ```bash
   jupyter notebook 01_eda_detective.ipynb
   ```

3. **Run feature engineering notebook:**

   ```bash
   jupyter notebook 02_feature_engineering.ipynb
   ```

   This will:

   - Encode categorical features (location, channel, device, type)
   - Apply log transformation to transaction amounts
   - Generate `full_data.csv` in the `processed/` folder

4. **Run model training notebook:**
   ```bash
   jupyter notebook 03_model_training.ipynb
   ```
   This will:
   - Split data into train/test sets
   - Save `train_data.csv` and `test_data.csv`
   - Train Isolation Forest model
   - Save model to `models/isolation_forest_model.pkl`

## Data Specifications

### Raw Data

- **Format:** CSV
- **Rows:** Transaction records
- **Columns:** 7 features (amount, hour, day_of_week, location, payment_channel, device_used, transaction_type)

### Processed Data

- **Format:** CSV
- **Features:** All categorical features label-encoded, amounts log-transformed
- **Target:** Anomaly score from Isolation Forest (-1 = fraud, 1 = normal)

## Data Privacy & Security

⚠️ **Important:**

- Never commit actual customer/transactional data to the repository
- Use `.gitignore` to prevent accidental commits
- Anonymize data before using in production
- Follow local data protection regulations (GDPR, NDPR, etc.)

## File Sizes

Expected sizes after processing:

- `full_data.csv` - 5-20 MB (depends on dataset size)
- `train_data.csv` - 3-15 MB
- `test_data.csv` - 1-5 MB

These are typically small enough to commit, but large datasets should use `.gitignore`.

## Troubleshooting

**Q: FileNotFoundError when running notebooks?**

- A: Ensure you're running notebooks from the `notebook/` directory
- Use relative paths like `../data/raw/`

**Q: Memory issues with large datasets?**

- A: Process data in chunks or increase available RAM
- Consider using `dask` for larger-than-memory datasets

**Q: Encoding mismatch errors?**

- A: Ensure all CSV files are UTF-8 encoded
- Check for special characters in location/channel names

## Next Steps

1. Place your dataset in `raw/` folder
2. Follow "Data Processing" section above
3. View results in `processed/` folder
4. Train model and test predictions via `src/app.py`

For more details, see the main [README.md](../README.md) and individual notebook documentation.
