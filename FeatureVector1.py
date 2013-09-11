
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

def main():
    
    blackList = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
                 '-', '=', '{', '}', '|', '[', ']', '\\', ']', ';', '\'', ':', '"',
                 ',', '.', '/', '<', '>', '?', 'to', 'a', 'is', 'and', 'be', 'the',
                 'of']
    
    sgm = RR('reut2-000.sgm')

    #print out all article names
    num = sgm.NumberOfReuters()

    #for i in range(0,num):
        #print(sgm.ExtractTagData(i,"TITLE"))
    
    #print(sgm.ExtractTagData(0, "TITLE"))
    #print

    #print frequuent nouns
    #for i in range(0, num):
        #print(sgm.ExtractTagData(i, "TITLE"))
        #printFrequentNouns(sgm.ExtractTagData(i, "BODY"))

    #tokenize the body - convert to lower casing
    body = sgm.ExtractTagData(0, "BODY").lower()
    tokens = nltk.word_tokenize(body)
    print tokens
    print
    
    #convert tokens to lower casing
    #for i in range(0, len(tokens)):
    #tokens[i] = tokens[i].lower()
            #print tokens
            #print

    #create the tags
    #tagged = nltk.pos_tag(tokens)
    ##entities = nltk.chunk.ne_chunk(tagged)
    #print tagged
    #print
    
    #create a tagged dictionary of nouns
    #tagdict = findtags('NN', tagged)
        #for tag in sorted(tagdict):
        #print tag, tagdict[tag]
        #print tagdict[tag]
    #print
    
    #the featured vector
    #featuredVector = []
    
    #construct the featured vector
    #for i in range(0, len(tagdict)):
        #if(not tagdict[i] in blackList):
            #featuredVector.append(tagdict[i])

    #print featuredVector
    #print

    #the dictionary
    d = {}

    #number of words
    numberOfWords = 0

    #put the tokens into a dictionary - count the number of words that
    #appear in the list
    numberOfTokens = len(tokens)
    for i in range(0, numberOfTokens):
        if not d.has_key(tokens[i]):
            d[tokens[i]] = 1
            numberOfWords = numberOfWords + 1
        elif d.has_key(tokens[i]):
            d[tokens[i]] = d[tokens[i]] + 1
            numberOfWords = numberOfWords + 1

    print(d)
    print

    print numberOfWords
    print

    keys = d.keys()
    print keys
    print

    lengthOfDict = len(d)
    print lengthOfDict
    print

    tupleList = []
    for i in range(0, lengthOfDict):
        #if not in the blackList then add it, dont add it otherwise
        if(not keys[i] in blackList):
            tuple = (format((d[keys[i]] / float(numberOfWords)), '0.10f'), d[keys[i]], keys[i])
            tupleList.append(tuple)
            print tuple

    print

    print sorted(tupleList)
    print

if __name__ == '__main__':
    main()
