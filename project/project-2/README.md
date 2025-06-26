# News-Classification-using-Natural-Language-Processing

A Machine Learning model which classifies weather the news given is genuine news or false news by the use of NLP (Natural Language Processing

# Details of Dataset

WE USED DATASETS -
• Fake.csv
• True.csv

COLUMNS : [Title, Text, Subject, Date]

Number of ROWS -
• Fake.csv consists of '23481' rows in total.
• True.csv consists of '21417' rows in total.

KNOW YOUR DATASET -

Subjects Involved :
• Political News
• Left-news
• Government News
• US_News
• Middle-east News
• World News

# Concepts Involved

1.  SUPERVISED LEARNING 

Supervised learning is where you have input variables (x) and an output variable (Y) and you use an algorithm to learn the mapping function from the input to the output Y = f(X). The goal is to approximate the mapping function so well that when you have new input data (x) that you can predict the output variables (Y) for that data. All classifications comes under supervised learning and our project will also be supervised learning i.e all category outputs comes under this " THIS PROJECT CLASSIFIES WHETHER NEWS IS GENUINE OR NOT "

2.  NLP – NATURAL LANGUAGE PROCESSING 

• NLP is a branch of Artificial Intelligence (AI) that studies how machines understand human language. 

• Its goal is to build systems that can make sense of text and perform tasks like translation, grammar checking, or topic classification.

NLP Libraries :

• NLTK  Natural Language Tool Kit (NLTK)  is an essential library supports tasks such as classification, stemming, tagging, parsing, semantic reasoning, and tokenization in Python. It’s basically your main tool for natural language processing and machine learning.

• SCI-KIT LEARNThis handy NLP library provides developers with a wide range of algorithms for building machine learning models. It offers many functions for using the bag-of-words method of creating features to tackle text classification problems.

3.  TEXT PREPROCESSING

Text Preprocessing Involves : 

• Tokenization - This process divides a large piece of continuous text into distinct units or tokens basically this process is often known as tokenization.

• Stemming - This is the idea of removing the suffix of a word and reducing different forms of a word to a core root.

• Stopword Removal - A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore.

4.  VECTORIZATION

Thescikit-learnlibrary offers easy-to-usetools to perform feature extraction of your text data that is Vectorization. The vectorization is a technique used to convert textual data to numerical format. Using vectorization, a matrix is created where each column represents a feature and each row represents an individual review. TF (Term Frequency) Term Frequency is defined as how frequently the word appear in the document.

    TF = No. of time word appear in the document / Total no. of word in the document

5.  CLASIFICATION ALGORITHMS

Passive-aggressive classification is one of the available incremental learning algorithms and it is very simple to implement.

• Passive : If the prediction is correct, keep the model and do not make any changes. i.e., the data in the example is not enough to cause any changes in the model.

• Aggressive : If the prediction is incorrect, make changes to the model. i.e., some change to the model may correct it.
