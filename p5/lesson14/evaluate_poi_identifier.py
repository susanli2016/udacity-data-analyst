#!/usr/bin/python
# -*- coding: cp1252 -*-


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.3, random_state=42)
clf=DecisionTreeClassifier()
clf.fit(features_train, labels_train)
clf.score(features_test, labels_test)

# How many POIs are in the test set for your POI identifier?
pred=clf.predict(features_test)
print sum(pred)
print len([e for e in labels_test if e==1.0])

# How many people total are in your test set?
print len(pred)

# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print (1-4.0/29)

# Precision and recall can help illuminate your performance better. 
# Use the precision_score and recall_score available in sklearn.metrics to compute those quantities.
# What’s the precision?
from sklearn.metrics import *
print precision_score(labels_test, pred)

# What's the recall of your POI identifier?
print recall_score(labels_test, pred)

# Here are some made-up predictions and true labels for a hypothetical test set; 
# fill in the following boxes to practice identifying true positives, false positives, true negatives, and false negatives. 
# Let’s use the convention that “1” signifies a positive result, and “0” a negative. 
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

cm = confusion_matrix(true_labels, predictions)
print cm, '\n'
print '{0} True positives'.format(cm[1][1])
print '{0} True negatives'.format(cm[0][0])
print '{0} False positives'.format(cm[0][1])
print '{0} False negatives'.format(cm[1][0])

#precision socre
print precision_score(true_labels, predictions)

#recall score 
print recall_score(true_labels, predictions)







