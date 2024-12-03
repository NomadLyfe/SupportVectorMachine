import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from SVM import SVM

X, y = datasets.make_blobs(
    n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state=40
)
y = np.where(y == 0, -1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

clf = SVM()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_pred == y_true) / len(y_true)
    return accuracy

acc = accuracy(y_test, pred)
print(acc)