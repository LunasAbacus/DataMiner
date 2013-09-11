
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
    body = re.sub("\\b\w\\b", " ", body)
    
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
    #print tag_fd
    #print

    #print [word + "/" + tag for (word, tag) in tag_fd if tag.startswith('V')]
    for (word, tag) in tag_fd:
        if(word not in blackListWords):
            featureVector.append(word)

    return featureVector[:10]

def main():

    featureVector = []
    
    with open('output4.txt','w') as wr:
        #for i in range(0,23):
        for i in range(0, 1):
            filename = "reut2-%s.sgm" % ("%03d" % i)
            print filename
            sgm = RR(filename)
            #print frequuent nouns
            for j in range(0, sgm.NumberOfReuters() - 1):
            #for j in range(0, 1):
                title = sgm.ExtractTagData(j, "TITLE")
                print title
                print
                featureVector = getFreqDist(sgm.ExtractTagData(j, "BODY"))
                print featureVector
                print
                wr.write("\n" + title)
                for k in range(0, len(featureVector)):
                    wr.write("\n" + featureVector[k])
                wr.write("\n")
    print 'done'

if __name__ == '__main__':
    main()
