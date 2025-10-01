import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the dataset
df = pd.read_csv('transactions_onehot_250.csv', index_col='TransactionID')

# Convert columns to integer type (if they are not already)
df = df.astype(bool)

# Find frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the top 10 rules, sorted by lift
print("Top 10 Association Rules:")
print(rules.sort_values('lift', ascending=False).head(10))
