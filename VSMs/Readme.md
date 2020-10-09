# VSMs based Tamil named entity recognition

folder structure

VSM
--- code
    --- config.py
    --- form.tpl
    --- service.py
    --- trainer.py
--- data
    --- train.txt
--- model
    --- clf.log
    --- clf.svm
    --- vocab.voc
--- performance
    --- logistic_regression.txt
    --- support_vector_machine.txt


Training:

1. Place the texts inside the folder "data", the word and tag has to be tab separated as given below,
	பாபநாசத்தில்	B-ENTERTAINMENT
	ஆஷா	B-PERSON
	சரத்	I-PERSON
	=	O
	போலீஸ்னா	O
	யார்னு	O
	தெரியுமா	O
	உனக்கு	O
	ரோஜா	B-ENTERTAINMENT
	வனம்	I-ENTERTAINMENT
	கமல்	B-PERSON
	டூ	O
	ஜோடி	O
	ஆஷா	B-PERSON 
        .
        .
        .

2. change the parameters in "config.py" in the folder "code"
	 It has the option to switch between Support Vector Machine and Logistic Regression

3. performance - It holds the performance that is achieved (10 fold 10 cross validation).
	logistic_regression.txt - gives the performance of logistic regression
	support_vector_machine.txt - gives the performance of support vector machine


Testing:

1. service.py - It serves light weight bottle based python service at port 8000  (http://localhost:8000), can be easilly configured.

2. model - model will be selected as algorithm choosed in "config.py" file





