import numpy as np
from sklearn import datasets
iris=datasets.load_iris()
from math import  sqrt
x_data=iris.data
x_label=iris.target
index=int(input("enter the index of test sample it should be between 0 and 149"))
test_data=iris.data[index]
#this function clculate distance between tow rows of data
def calculate_distance(x,y):
 for i in range(len(x)):
     distanc=0.0
     distanc= distanc +(x[i]-y[i])**2
     return sqrt(distanc)
 #this fuction find the  nearest neghbor you enter to your test_data and labeling them and sorting
def neighbor_get(x_data,label,test_data,k):
     distanc=[]
     for index in range(len (x_data)) :
         d=calculate_distance(test_data,x_data[index])
         distanc.append((x_data[index],d,label[index]))
     distanc.sort(key=lambda x:x[1])
     neighbors=distanc[:k]
     return neighbors
#this function predict the target of your test data relating  to nearset neighbor you found
def predict_classfy(x_data,label,test,k):
    k=k
    neighbors=neighbor_get(x_data,label,test,k)
    valu_out=[row[-1]for row in neighbors]
    predict=max(set(valu_out),key=valu_out.count)
    return predict
#enter number of key print the neighbor and the prediction
k=int(input("enter number of nearest key remmber if the number is big the prediction is more accurecy"))
neighbors=neighbor_get(x_data,x_label,test_data,k)
for neighbor in neighbors:
    print (neighbor)
prediction =predict_classfy(x_data,x_label,test_data,k)
if prediction==0:
    typ='setosa'
elif prediction==1:
    typ='virginca'
else:typ='versicolor'
print( ' the classifiction of test data is' , prediction," ",typ)