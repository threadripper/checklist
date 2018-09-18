import cv2
import numpy as np
import matplotlib.pyplot as plt
train_labels=[]
num=50
b=8
train=np.random.randint(0,10,(num,2)).astype(np.float32)
for i in range(num):
           if train[i,0]+train[i,1]>b:
              plt.plot(train[i,0],train[i,1],'r*')
              train_labels.append([1])
           else:
              plt.plot(train[i,0],train[i,1],'g*')
              train_labels.append([0])
knn = cv2.ml.KNearest_create()
train_labels=np.array(train_labels)
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
test=np.random.randint(0,10,(1,2)).astype(np.float32)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
if ret==1.0:
                  plt.plot(test[0,0],test[0,1],'ro')
else:
                  plt.plot(test[0,0],test[0,1],'go')
plt.plot([0,b],[b,0])
plt.show()