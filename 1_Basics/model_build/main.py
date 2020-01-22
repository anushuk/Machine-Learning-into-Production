
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
import os
import pickle

#for ignoring any warnings
import warnings
warnings.filterwarnings("ignore")

#getting current path
cwd = os.getcwd()

#dataset path
Dataset_path = os.path.join(cwd,'..','..','Data','Social_Network_Ads.csv')

# Importing the dataset
Dataset_path
dataset = pd.read_csv(Dataset_path)

#columns ('Gender','Age',' EstimatedSalary')
X = dataset.iloc[:, [1,2, 3]].values

#columns ('Purchased')
y = dataset.iloc[:, 4].values




#clearly "Gender"  column need to be changed into numerical variables
label_x=LabelEncoder()
X[:,0]=label_x.fit_transform(X[:,0])

#getting the mapping of numerical variables
le_name_mapping = dict(zip(label_x.classes_, label_x.transform(label_x.classes_)))

#Saving mapping {'Female':0, 'Male':1} into a file for future reference
file_path = os.path.join(cwd,'..','Flask_app','pklobjects','info.txt')
with open(file_path,'w') as fil:
    fil.write('Information about model'+'\n')
    fil.write("Gender mapping"+str(le_name_mapping))



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#saving scaled object
scaler_path=os.path.join(cwd,'..','Flask_app','pklobjects','scaler.pkl')
pickle.dump(sc,open(scaler_path,'wb'))

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#printing confusion matrix to the console
cm=confusion_matrix(y_test,y_pred)
print(cm)

#evaluating various metrics
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)

print('Accuracy Score: {0:0.2f}, Precion Score: {1:0.2f}, Recall Score :{2:0.2f}, F1 Score : {3:0.2f}'.format(
      accuracy,precision,recall,f1))


#Saving the model as pickle object
saved_model_path=os.path.join(cwd,'..','Flask_app','pklobjects','model.pkl')
pickle.dump(classifier,open(saved_model_path,'wb'))
