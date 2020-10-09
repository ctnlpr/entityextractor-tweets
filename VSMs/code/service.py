# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("always")
from sklearn.externals import joblib
from bottle import Bottle, template, request
import config
import load_model
import numpy as np
import random
random.seed(7)


# loading word2vec model
w2v_model = load_model.get_w2v()


# loading classifier model
classifier_path = config.classifier_path
classifier = joblib.load(classifier_path)

def data_cleaning(term):
    if len(term) > 3:
        term = term.replace('.','')
        term = term.replace(',','')
        term = term.replace('-','')
        term = term.replace('?','')
        term = term.replace('_','')
        term = term.replace('#','')
    return term

def get_word_features(text):
    test_words = text.split()
    testMatrix = []
    for word in test_words:
        word = data_cleaning(word)
        try:
            vector = w2v_model[word].tolist()
        except KeyError:
            vector = np.random.rand(1,300).tolist()[0]
        testMatrix.append(vector)
    testMatrix = np.asmatrix(testMatrix)
    return testMatrix


app = Bottle()

@app.route('/')
def index():
    """Home Page"""
    
    return template("form.tpl", info="",stm="")

@app.route('/api/formhandler', method='POST')

def formhandler():
    temp_response = []
    sentence = request.forms.get('first')
    
    feature_matrix = get_word_features(sentence)
    
    labels = classifier.predict(feature_matrix)
    nerTags = labels.tolist()
    terms = sentence.split()
   

    for t1, t2 in zip(terms, nerTags):
        temp = t1 + '_' + t2
        temp_response.append(temp)
    info = sentence
    stm = '              '.join(temp_response)
    
    return template("form.tpl", info=info, stm=stm)

if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=False)
