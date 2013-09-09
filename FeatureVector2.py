#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     09/09/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR
import nltk
from decimal import Decimal

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

def extractFeatureVector(body):
    
    blackList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
                 '-', '=', '{', '}', '|', '[', ']', '\\', ']', ';', '\'', ':', '"',
                 ',', '.', '/', '<', '>', '?', 'to', 'a', 'is', 'and', 'be', 'the',
                 'of']
    
    featureVector = []
    
    tokens = nltk.word_tokenize(body)
    tagged = nltk.pos_tag(tokens)
    #tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
    #tagged = tagger.tag(tokens)
    #print tagged
    tagdict = findtags('NN', tagged)
    for tag in sorted(tagdict):
        for i in tagdict[tag]:
            if(not i in blackList):
                featureVector.append(i)
        #print tagdict[tag]
    #print

    return featureVector

def main():

    #parse the data from the file
    sgm = RR('reut2-000.sgm')
    
    #number of reuters
    numberOfReuters = sgm.NumberOfReuters()
    
    #print frequuent nouns
    for i in range(0, 1):
        print(sgm.ExtractTagData(i, "TITLE"))
        #printFrequentNouns(sgm.ExtractTagData(i, "BODY"))
        featureVector = extractFeatureVector(sgm.ExtractTagData(i, "BODY"))
        print featureVector

if __name__ == '__main__':
    main()
