from bottle import Bottle, template, request
import config
from sklearn.externals import joblib


vocab_path = '../model/vocab.voc'
classifier_path = config.classifier_path
train_path = config.train_path

classifier = joblib.load(classifier_path)

word_model = joblib.load(vocab_path)

model = {}

read_file = open(train_path, 'r+')
for line in read_file:
    line = line.strip()
    try:
        word, tag = line.split('\t')
        if tag == 'START':
            pass
        else:
            model[word] = tag
    except ValueError:
        pass
read_file.close()




def get_word_features(text):
    test_words = text.split()
    testMatrix = word_model.transform(test_words)
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
        try:
            t2 = model[t1]
        except KeyError:
            pass
        temp = t1 + '_' + t2
        temp_response.append(temp)

    info = sentence
    stm = '              '.join(temp_response)
   
    return template("form.tpl", info=info, stm=stm)

if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=False)
