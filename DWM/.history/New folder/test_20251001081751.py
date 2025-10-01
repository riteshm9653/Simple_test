from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
X = [
[0, 0], [1, 1], [1, 0], [0, 1],
[2, 1], [2, 0], [3, 3], [3, 2],
[4, 4], [4, 3]
]
y = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1]

dt= DecisionTreeClassifier()


pred= dt.predict([[1,0],[0,2],[5,3]])
