import pandas as pd
import os

# Full path to the Excel file
file_path = 'C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Data Analyst Intern Assignment - Excel.xlsx'

# Load each sheet into a DataFrame
user_details = pd.read_excel(file_path, sheet_name='UserDetails.csv')
cooking_sessions = pd.read_excel(file_path, sheet_name='CookingSessions.csv')
order_details = pd.read_excel(file_path, sheet_name='OrderDetails.csv')

# Clean UserDetails
user_details.drop_duplicates(inplace=True)  # Remove duplicates
user_details.dropna(inplace=True)  # Remove missing values

# Clean CookingSessions
cooking_sessions.drop_duplicates(inplace=True)  # Remove duplicates
cooking_sessions.dropna(inplace=True)  # Remove missing values

# Clean OrderDetails
order_details.drop_duplicates(inplace=True)  # Remove duplicates
order_details.dropna(inplace=True)  # Remove missing values

# Ensure the 'data' directory exists, if not, create it
output_dir = 'C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data'
os.makedirs(output_dir, exist_ok=True)

# Save cleaned data
user_details.to_csv(f'{output_dir}/Cleaned_UserDetails.csv', index=False)
cooking_sessions.to_csv(f'{output_dir}/Cleaned_CookingSessions.csv', index=False)
order_details.to_csv(f'{output_dir}/Cleaned_OrderDetails.csv', index=False)

print("Data cleaned and saved successfully!")
