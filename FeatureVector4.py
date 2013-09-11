#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     07/09/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR
import nltk
from decimal import Decimal
import re

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

def printFrequentNouns(body):
    tokens = nltk.word_tokenize(body)
    tagged = nltk.pos_tag(tokens)
    #tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
    #tagged = tagger.tag(tokens)
    #print tagged
    tagdict = findtags('NN', tagged)
    for tag in sorted(tagdict):
        print tagdict[tag]
    print

def getFreqDist(body):
    
    blackList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
                 '-', '=', '{', '}', '|', '[', ']', '\\', ']', ';', '\'', ':', '"',
                 ',', '.', '/', '<', '>', '?', 'to', 'a', 'is', 'and', 'be', 'the',
                 'of']
    
    blackListWords = []
    
    featureVector = []
    
    body = re.sub("[\d]"," ", body)
    body = re.sub("[^\w]"," ", body)
    body = re.sub("\\b\w\w\\b", " ", body)
    #body = re.sub("\\b\w\\b", " ", body)
    
    #create the black list words
    with open('stopwords.txt') as f:
        for line in f:
            blackListWords.append(line.rstrip())

    #split up the word into tokens
    tokens = nltk.word_tokenize(body)
    print tokens
    print

    #create the tags
    tagged = nltk.pos_tag(tokens)
    ##entities = nltk.chunk.ne_chunk(tagged)
    print tagged
    print

    taggedCleaned = []
    for i in range(0, len(tagged)):
        if not tagged[i][0] in blackListWords:
            taggedCleaned.append(tagged[i])
    
    #get the frequency distribution
    tag_fd = nltk.FreqDist(tagged)
    print tag_fd
    print

    #print [word + "/" + tag for (word, tag) in tag_fd if tag.startswith('V')]
    for (word, tag) in tag_fd:
        if(word not in blackListWords):
            featureVector.append(word)

    return featureVector[:10]

def main():

    sgm = RR('reut2-000.sgm')

    #print out all article names
    num = sgm.NumberOfReuters()

    #for i in range(0,num):
        #print(sgm.ExtractTagData(i,"TITLE"))
    
    #print(sgm.ExtractTagData(0, "TITLE"))
    #print

    featureVector = []
    
    #print frequuent nouns
    for i in range(0, 3):
        print(sgm.ExtractTagData(i, "TITLE"))
        featureVector = getFreqDist(sgm.ExtractTagData(i, "BODY"))
        print featureVector

if __name__ == '__main__':
    main()
