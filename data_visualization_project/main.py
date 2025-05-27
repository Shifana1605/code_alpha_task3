import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file
df = pd.read_csv(r'C:\Users\mfshi\data_visualization_project\data.csv')

# Set up the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))

# Create the bar plot
sns.barplot(x='Month', y='Sales', data=df, palette='Blues_d')

# Add title and labels
plt.title('Monthly Sales Overview')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.tight_layout()

# ✅ Step 5: Save and show the plot
plt.savefig('sales_chart.png')
plt.show()
