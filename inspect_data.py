import pandas as pd
import os

# Let's find the first file inside your unzipped folder
# Replace 'pricer-output-2026-05-11_2026-06-10' if your folder name is slightly different
data_folder = "pricer-output-2026-05-11_2026-06-10"
files = [f for f in os.listdir(data_folder) if f.endswith('.parquet')]

if files:
    first_file_path = os.path.join(data_folder, files[0])
    print(f"Reading sample file: {files[0]}")
    
    # Read just the top 5 rows to see the column structure
    df = pd.read_parquet(first_file_path).head()
    print("\n--- Columns and Data Sample ---")
    print(df.to_string())
else:
    print("No parquet files found! Double check the folder name.")
    