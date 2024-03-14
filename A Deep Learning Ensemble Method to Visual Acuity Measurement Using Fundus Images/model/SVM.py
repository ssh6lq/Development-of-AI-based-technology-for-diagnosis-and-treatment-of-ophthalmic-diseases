import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

def data_Set(classes, dir, x, y, z ):
    flat_data_arr=[] #input array
    target_arr=[] #output array
    for i in classes: 
        path=os.path.join(dir,i)
        for img in os.listdir(path):
            img_array=imread(os.path.join(path,img))
            img_resized=resize(img_array,(x,y,z))
            flat_data_arr.append(img_resized.flatten())
            target_arr.append(Categories.index(i))
    flat_data=np.array(flat_data_arr)
    target=np.array(target_arr)
    df=pd.DataFrame(flat_data) #dataframe
    df['Target']=target
    x_data=df.iloc[:,:-1] #input data 
    y_data=df.iloc[:,-1] #output data
    return x_data, y_data

def get_clf_eval(y_test, y_pred=None):
    confusion = confusion_matrix(y_test, y_pred, labels=[True, False])
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, labels=[True, False])
    recall = recall_score(y_test, y_pred)
    F1 = f1_score(y_test, y_pred, labels=[True, False])

    print("오차행렬:\n", confusion)
    print("\n정확도: {:.4f}".format(accuracy))
    print("정밀도: {:.4f}".format(precision))
    print("재현율: {:.4f}".format(recall))
    print("F1: {:.4f}".format(F1))


x_train, y_train = data_Set([1,2],'./Aug_2',32,32,3)
x_test, y_test = data_Set([1,2],'./Origin',32,32,3)

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
#--------------------------------------------학습한 모델을 pickle변수로 저장
model_from_pickle = pickle.loads(saved_model)

#model_from_pickle.predict(x_test)
