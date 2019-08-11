#importing important Libraries
import pandas as pd
import numpy as np
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
from estimators import custom_estimator  #importing custom_estimator class from estimators.py
from estimators import ThresholdBinarizer #importing ThresholdBinarizer class from estimators.py
from sklearn.metrics import confusion_matrix

import warnings
warnings.filterwarnings("ignore")

cwd = os.getcwd()

Dataset_path = os.path.join(cwd,'..','Data','Social_Network_Ads.csv')
# Importing the dataset
dataset = pd.read_csv(Dataset_path)

X = dataset.iloc[:, [1, 2, 3]].values # It includes coloumns as "Age" and "EstimatedSalary"

y = dataset.iloc[:, 4].values #  It includes column as "Purchased"

#clearly "Gender"  column need to be changed into numerical variables
label_x=LabelEncoder()
X[:,0]=label_x.fit_transform(X[:,0])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


################################Building Model ##############3333



model=custom_estimator() #Calling the custom_estimator class with appropiate classifier

model.fit(X_train,y_train) # traing the model

y_prob=model.predict_proba(X_test) #getting the predicted probality of each class



################## optimizing the model #########################

binar=ThresholdBinarizer(model) #Calling the the ThresholdBinarizer class with the trained model

binar.fit(X_test,y_test)

y_pred, gini, th =binar.transform(X_test,y_test) #returns the predicted value, gini Coefficient, optimal threshold value

#metrics

cm=confusion_matrix(y_test,y_pred)
print(cm)

#evaluating various metrics
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)

print('Accuracy Score: {0:0.2f}, Precion Score: {1:0.2f}, Recall Score :{2:0.2f}, F1 Score : {3:0.2f}, Gini Coefficient : {4:0.2f}, Threshold Value : {5:0.2f}  '.format(
      accuracy,precision,recall,f1,gini,th))
