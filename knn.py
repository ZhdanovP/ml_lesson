from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_datase = load_iris()

X_train, X_test, Y_train, Y_test = 
	train_test_split(iris_datase["data"], iris_datase["target"], random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, Y_train)

x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = kn.predict(x_new)

print("Test score: {:.2f}".format(knn.score(X_test, Y_test)))