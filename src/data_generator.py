import pandas as pd
import numpy as np
from datetime import timedelta, datetime

# Set random seed for reproducibility
np.random.seed(42)

# Create synthetic data
data = {
    'Step_ID': np.random.choice(['Assembly', 'Welding', 'Inspection', 'Testing'], size=100),
    'Duration': np.random.uniform(1, 10, size=100),  # Random duration between 1 and 10 hours
    'Start_Time': pd.date_range(start='2023-09-01', periods=100, freq='h'),  # Use 'h' instead of 'H'
    'End_Time': pd.date_range(start='2023-09-01', periods=100, freq='h') + pd.to_timedelta(np.random.randint(1, 10, size=100), unit='h'),
    'Operator_ID': np.random.randint(100, 110, size=100),  # Random operator IDs
    'Machine_ID': np.random.randint(200, 210, size=100),   # Random machine IDs
    'Fault_Flag': np.random.choice([0, 1], size=100, p=[0.8, 0.2])  # 20% chance of fault
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('../dataset/generated/synthetic_manufacturing_data.csv', index=False)
print("Data generated.")
