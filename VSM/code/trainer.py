from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.externals import joblib
import numpy as np
import config

train_path = config.train_path

# getting text and labels from train file

model = {}
words = list()
labels = list()
read_file = open(train_path, 'r+')
for line in read_file:
    line = line.strip()
    try:
        word, tag = line.split('\t')
        if tag == 'START':
            pass
        else:
            words.append(word)
            labels.append(tag)
            model[word] = tag
    except ValueError:
        pass
read_file.close()


vocabulary = CountVectorizer(binary=True)
trainMatrix = vocabulary.fit_transform(words)
print(trainMatrix.shape)
joblib.dump(vocabulary, '../model/vocab.voc')


if config.classifier == 'LOG':
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression().fit(trainMatrix, labels)
    print('training accuracy is: ', clf.score(trainMatrix, labels))
    joblib.dump(clf, config.classifier_path)
    def do_10_cv():
        labelList = np.array(labels)
        from sklearn.model_selection import KFold
        kf = KFold(n_splits=10)
        kf.get_n_splits(trainMatrix)
        i = 1
        for train_index, test_index in kf.split(trainMatrix):
            X_train, X_test = trainMatrix[train_index], trainMatrix[test_index]
            y_train, y_test = labelList[train_index], labelList[test_index]
            clf = LogisticRegression().fit(X_train, y_train)
            print('for cross validation', i, 'accuracy =', clf.score(X_test, y_test))
            i = i + 1
    do_10_cv()
elif config.classifier == 'SVM':
    from sklearn import svm
    clf = svm.SVC(kernel='rbf').fit(trainMatrix, labels)
    print('training accuracy is: ', clf.score(trainMatrix, labels))
    joblib.dump(clf, config.classifier_path)
    def do_10_cv():
        labelList = np.array(labels)
        from sklearn.model_selection import KFold
        kf = KFold(n_splits=10)
        kf.get_n_splits(trainMatrix)
        i = 1
        for train_index, test_index in kf.split(trainMatrix):
            X_train, X_test = trainMatrix[train_index], trainMatrix[test_index]
            y_train, y_test = labelList[train_index], labelList[test_index]
            clf = svm.SVC(kernel='rbf').fit(X_train, y_train)
            print('for cross validation', i, 'accuracy =', clf.score(X_test, y_test))
            i = i + 1
    do_10_cv()
else:
    pass
