import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import time
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#train set
Categories=['1','2']
flat_data_arr=[] #input array
target_arr=[] #output array
datadir='./Aug_2'
#path which contains all the categories of images
for i in Categories: 
    print(f'loading... category : {i}')
    path=os.path.join(datadir,i)
    for img in os.listdir(path):
        img_array=imread(os.path.join(path,img))
        img_resized=resize(img_array,(32,32,3))
        flat_data_arr.append(img_resized.flatten())
        target_arr.append(Categories.index(i))
    print(f'loaded category:{i} successfully')
flat_data=np.array(flat_data_arr)
target=np.array(target_arr)
df=pd.DataFrame(flat_data) #dataframe
df['Target']=target
x_train=df.iloc[:,:-1] #input data 
y_train=df.iloc[:,-1] #output data

#testset
Categories=['1','2']
flat_data_arr=[] #input array
target_arr=[] #output array
datadir='./Origin'
#path which contains all the categories of images
for i in Categories: 
    print(f'loading... category : {i}')
    path=os.path.join(datadir,i)
    for img in os.listdir(path):
        img_array=imread(os.path.join(path,img))
        img_resized=resize(img_array,(32,32,3))
        flat_data_arr.append(img_resized.flatten())
        target_arr.append(Categories.index(i))
    print(f'loaded category:{i} successfully')
flat_data=np.array(flat_data_arr)
target=np.array(target_arr)
df=pd.DataFrame(flat_data) #dataframe
df['Target']=target
x_test=df.iloc[:,:-1] #input data 
y_test=df.iloc[:,-1] #output data

#train_test_split
scaler=MinMaxScaler().fit(x_train)
x_train=scaler.transform(x_train)

x_train,x_test,y_train,y_test=train_test_split(x_train,y_train,test_size=0.20,random_state=77,stratify=y_train)
print('Splitted Successfully')

#SVM MODEL
for thisGamma in [.1]:
    for thisC in [0.1,1,10,50,100]:
        model_1=SVC(kernel="rbf", C=thisC,
                   gamma=thisGamma).fit(x_train, y_train)
        model_1train=model_1.score(x_train,y_train)
        model_1test=model_1.score(x_test,y_test)
        
        print("RBF SVM : C:{}, gamma:{},training score:{:2f},test score:{:2f} \n".format(thisC, thisGamma, model_1train, model_1test))  

#model_save
saved_model = pickle.dumps(model_1) #32x32
#--------------------------------------------학습한 모델을 pickle변수로 저장한 것
model_from_pickle = pickle.loads(saved_model)

#model_from_pickle.predict(x_test)
