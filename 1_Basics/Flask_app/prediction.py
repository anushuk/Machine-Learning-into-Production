
import os
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


cwd_path= os.getcwd() #getting current path

#loading the saved model
clf=pickle.load(open(os.path.join(cwd_path,'pklobjects','model.pkl'),'rb'))

#loading the saved scaler object
scaler=pickle.load(open(os.path.join(cwd_path,'pklobjects','scaler.pkl'),'rb'))


def predic(X):

    X=np.array(X).reshape(1,-1) #tranforming list into 2D array

    X_test = scaler.transform(X) #scaling the values

    result = clf.predict(X_test) #prediction

    return int(result[0]) #returning the result
