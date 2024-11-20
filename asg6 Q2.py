# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:07:06 2024

@author: FIEM
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris=datasets.load_iris()
X=iris.data
Y=iris.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

model=SVC(kernel='linear')

model.fit(X_train,Y_train)

Y_pred=model.predict(X_test)
accuracy = accuracy_score(Y_test,Y_pred)
print(f'Accuracy:{accuracy*100:.2f}%')
