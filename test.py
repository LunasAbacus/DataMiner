#!/usr/bin/evn python

import nltk
import re
import random

from nltk.corpus import movie_reviews

def gender_features(word):
    return {'last_letter': word[-1]}

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    #print document
    #print
    document_words = set(document)
    #print document_words
    #print
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
        #print features
        #print
    return features

def main():

    #from nltk.corpus import names
    #names = ([(name, 'male') for name in names.words('male.txt')] +
    #         [(name, 'female') for name in names.words('female.txt')])
    #random.shuffle(names)
    #print names
    #print
    
    #train_set = names
    #classifier = nltk.NaiveBayesClassifier.train(train_set)
    #name = classifier.classify("Jaime")
    #print name
    
    #featuresets = [(gender_features(n), g) for (n,g) in names]
    #train_set = [(gender_features(n), g) for (n, g) in names]
    #train_set, test_set = featuresets[500:], featuresets[:500]
    #print train_set
    #print
    
    #classifier = nltk.NaiveBayesClassifier.train(train_set)
    #name = classifier.classify(gender_features('Neo'))
    #print name
    
    documents = [(list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    
    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    print train_set
    print
    
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    print nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(5)
    
    print 'done'

if __name__ == '__main__':
    main()