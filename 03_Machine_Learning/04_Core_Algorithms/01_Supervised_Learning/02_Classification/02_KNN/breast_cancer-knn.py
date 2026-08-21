#===================================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

scaler = StandardScaler()
knn = KNeighborsClassifier(n_neighbors=5)

#===================================================================================


df = pd.read_csv("/home/ipartzix/ML-dataset/Breast_Cancer_Wisconsin_dataset.csv")
df = df.drop(columns=["id","Unnamed: 32"]) # remove two this columns from this dataframe 

print(df.head())
print(df.columns.tolist())

print(df.shape)

print("_____________________________________________________________________________")

X = df.iloc[ :, 1:]
y = df.iloc[:,0]

#====================================================================================

X_train ,X_test ,y_train ,y_test =train_test_split(X,y,train_size=0.8, random_state=42)
print(X_train.shape)

print(X_train)
print("--------------------------------------")

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

print(X_test)
print(X_train.shape)

knn.fit(X_train,y_train)

y_pred =knn.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)