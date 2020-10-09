# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("always")

# train file path
train_path = '../data/train.txt'



# select 'SVM' for loading and training Support Vector Machine based classifier or
# select 'LOG' for loading and training Logistic Regression based classifier
# default is Logistic Regression

classifier = 'SVM' 
#classifier = 'LOG'

if classifier == 'SVM':
    classifier_path = '../model/clf.svm'
elif classifier == 'LOG':
    classifier_path = '../model/clf.log'
else:
    classifier_path = '../model/clf.log'


