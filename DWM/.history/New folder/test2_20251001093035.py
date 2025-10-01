
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
X = np.array([[1,2],[1,4],[1,0],
[10,2],[10,4],[10,0]])
linked = linkage(X, method='ward')
print("Linkage Matrix:\n", linked)
dendrogram(linked)
plt.show()
