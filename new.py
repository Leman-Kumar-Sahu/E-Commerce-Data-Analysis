# Process the uploaded dataset to create repeating Customer_IDs (101–1100)
import pandas as pd
import numpy as np

df = pd.read_csv("customer_shopping_behavior.csv")
n_rows = len(df)

# Create 1000 unique IDs from 101 to 1100
customer_ids = np.arange(101, 1101)

# Repeat IDs randomly to fill all rows
np.random.seed(42)
new_ids = np.random.choice(customer_ids, size=n_rows, replace=True)

df["Customer ID"] = new_ids

# Save the modified dataset
output_csv = "shopping_behavior_modified.csv"
output_xlsx = "shopping_behavior_modified.xlsx"

df.to_csv(output_csv, index=False)
df.to_excel(output_xlsx, index=False)

# output_csv, output_xlsx