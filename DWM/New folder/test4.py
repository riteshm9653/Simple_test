from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
X = np.array([[1],[2],[3],[4],[1.5]])
y = np.array([2,3,7,8,4])
model = LinearRegression().fit(X, y)
model.predict([[5]])
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.show()
