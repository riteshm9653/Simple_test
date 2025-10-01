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

[Text(0.4, 0.875, 'x[0] <= 0.5\ngini = 0.42\nsamples = 10\nvalue = [3, 7]'),
 Text(0.2, 0.625, 'gini = 0.0\nsamples = 2\nvalue = [2, 0]'),
 Text(0.30000000000000004, 0.75, 'True  '),
 Text(0.6, 0.625, 'x[1] <= 0.5\ngini = 0.219\nsamples = 8\nvalue = [1, 7]'),
 Text(0.5, 0.75, '  False'),
 Text(0.4, 0.375, 'x[0] <= 1.5\ngini = 0.5\nsamples = 2\nvalue = [1, 1]'),
 Text(0.2, 0.125, 'gini = 0.0\nsamples = 1\nvalue = [0, 1]'),
 Text(0.6, 0.125, 'gini = 0.0\nsamples = 1\nvalue = [1, 0]'),
 Text(0.8, 0.375, 'gini = 0.0\nsamples = 6\nvalue = [0, 6]')]
