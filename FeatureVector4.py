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

    #split up the word into tokens
    tokens = nltk.word_tokenize(body)
    print tokens
    print

    #create the tags
    tagged = nltk.pos_tag(tokens)
    ##entities = nltk.chunk.ne_chunk(tagged)
    print tagged
    print
    
    #get the frequency distribution
    tag_fd = nltk.FreqDist(tagged)
    print tag_fd
    print
    

def main():

    sgm = RR('reut2-000.sgm')

    #print out all article names
    num = sgm.NumberOfReuters()

    #for i in range(0,num):
        #print(sgm.ExtractTagData(i,"TITLE"))
    
    #print(sgm.ExtractTagData(0, "TITLE"))
    #print

    #print frequuent nouns
    for i in range(0, 2):
        print(sgm.ExtractTagData(i, "TITLE"))
        getFreqDist(sgm.ExtractTagData(i, "BODY"))

if __name__ == '__main__':
    main()
