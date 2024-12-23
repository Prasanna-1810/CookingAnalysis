import pandas as pd

# Load the Excel file with corrected file path
file_path = 'C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Data Analyst Intern Assignment - Excel.xlsx'

# Load each sheet into a DataFrame
user_details = pd.read_excel(file_path, sheet_name='UserDetails.csv')
cooking_sessions = pd.read_excel(file_path, sheet_name='CookingSessions.csv')
order_details = pd.read_excel(file_path, sheet_name='OrderDetails.csv')

# Display basic information
print("User Details:\n", user_details.head())
print("\nCooking Sessions:\n", cooking_sessions.head())
print("\nOrder Details:\n", order_details.head())
