#importing important Libraries
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score



# custom_estimator class used for binary classification
class  custom_estimator(BaseEstimator, ClassifierMixin):
    def __init__(self, estimator=LogisticRegression()):
        self.estimator = estimator #initalizing the given classifier

    #fitting the classifier
    def fit(self, X, y):
        self.fitted_estimator_ = self.estimator.fit(X, y)
        return self

    #returns binary prediction results
    def predict(self, X):
        return self.fitted_estimator_.predict(X)

    #returns probality of  prediction results
    def predict_proba(self, X):
        return self.fitted_estimator_.predict_proba(X)




#It optimises the threshold with respect to the Gini impurity
class ThresholdBinarizer(BaseEstimator, TransformerMixin):

    def __init__(self, clf = None):
        self.clf = clf

    def fit(self, X, y):
        return self

    def threshold(self,X,y):
        self.prediction_=  self.clf.predict_proba(X)[:,1]
        self.fpr, self.tpr, self.thresholds = roc_curve(y, self.prediction_)
        self.scores = []
        for thresh in self.thresholds:
            self.scores.append((2*roc_auc_score(y,
                                     [1 if m > thresh else 0 for m in self.prediction_]))-1)

        self.accuracies = np.array(self.scores)
        self.max_accuracy = self.accuracies.max()
        self.max_accuracy_threshold =  self.thresholds[self.accuracies.argmax()]
        return self.max_accuracy_threshold, self.prediction_, self.max_accuracy

    def transform(self,X, y):
        th, pred, gini =self.threshold(X,y)
        y_pred=np.array([1 if m > th else 0 for m in pred])


        return y_pred, gini ,th
