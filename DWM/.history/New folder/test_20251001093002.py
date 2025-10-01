# Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

X = [
    [0, 0], [1, 1], [1, 0], [0, 1],
    [2, 1], [2, 0], [3, 3], [3, 2],
    [4, 4], [4, 3]
]
y = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1]

# Create and train the decision tree
dt = DecisionTreeClassifier()
dt.fit(X, y)

# Make predictions
test_data = [[1, 0], [0, 2], [5, 3]]
pred = dt.predict(test_data)

# Print the predictions
print("Test data:", test_data)
print("Predictions:", pred)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(dt, filled=True, feature_names=['Feature 1', 'Feature 2'],
               class_names=['Class 0', 'Class 1'])
plt.title('Decision Tree Visualization')
plt.show()
