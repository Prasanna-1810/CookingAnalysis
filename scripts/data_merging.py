import pandas as pd

# Absolute path to the cleaned data files
user_details = pd.read_csv('C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Cleaned_UserDetails.csv')
cooking_sessions = pd.read_csv('C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Cleaned_CookingSessions.csv')
order_details = pd.read_csv('C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Cleaned_OrderDetails.csv')

# Merge datasets
merged_data = pd.merge(cooking_sessions, user_details, on='User ID')
merged_data = pd.merge(merged_data, order_details, on=['User ID', 'Dish Name'])

# Save merged data
merged_data.to_csv('C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Merged_Data.csv', index=False)

print("Datasets merged and saved successfully!")
