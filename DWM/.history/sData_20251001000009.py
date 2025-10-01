import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sales.csv')

# Convert 'Time' to a categorical type for proper plotting
df['Time'] = df['Time'].astype(str)

# Create a line plot of sales over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Time', y='Sales', hue='Product', style='Region', marker='o')
plt.title('Sales Trend by Product and Region')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.legend(title='Product and Region')
plt.show()
