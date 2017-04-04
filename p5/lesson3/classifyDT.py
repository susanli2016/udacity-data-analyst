from sklearn import tree
def classify(features_train, labels_train):
    ### your code goes here--should return a trained decision tree classifier
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    return clf
