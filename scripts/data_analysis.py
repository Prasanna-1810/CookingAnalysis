import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Absolute path to the merged data file
merged_data_path = 'C:/Users/prasa/OneDrive/Desktop/prasanna/CookingAnalysis/Data/Merged_Data.csv'

# Load merged data
merged_data = pd.read_csv(merged_data_path)

# Popular dishes: top 10 most frequent dishes
popular_dishes = merged_data['Dish Name'].value_counts().head(10)

# Ensure the 'outputs' directory exists, if not, create it
output_dir = '../outputs'
os.makedirs(output_dir, exist_ok=True)

# Plot dish popularity
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_dishes.values, y=popular_dishes.index)
plt.title("Top 10 Popular Dishes")
plt.xlabel("Frequency")
plt.ylabel("Dish Name")
plt.savefig(f'{output_dir}/popular_dishes.png')  # Save the plot
plt.show()  # Show the plot
