
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR
import nltk
from decimal import Decimal

def getTags(tag_prefix, tagged_text):
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
    
    blackListWords = []
    
    #create the black list words
    with open('stopwords.txt') as f:
        for line in f:
            blackListWords.append(line.rstrip())
    
    tokens = nltk.word_tokenize(body)
    tagged = nltk.pos_tag(tokens)
    #tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
    #tagged = tagger.tag(tokens)
    #print tagged
    tagdict = getTags('NN', tagged)
    for tag in sorted(tagdict):
        for i in tagdict[tag]:
            if(not i in blackList) and (not i in blackListWords):
                featureVector.append(i)
        #print tagdict[tag]
    #print

    return featureVector

def main():

    with open('output2.txt','w') as wr:
        #for i in range(0,23):
        for i in range(0, 1):
            filename = "reut2-%s.sgm" % ("%03d" % i)
            print filename
            sgm = RR(filename)
            #print frequuent nouns
            for j in range(0, sgm.NumberOfReuters() - 1):
                title = sgm.ExtractTagData(j, "TITLE")
                print title
                #printFrequentNouns(sgm.ExtractTagData(i, "BODY"))
                featureVector = extractFeatureVector(sgm.ExtractTagData(j, "BODY"))
                print featureVector
                print

                wr.write("\n" + title)
                for k in range(0, len(featureVector)):
                    wr.write("\n" + featureVector[k])
                wr.write("\n")
    
    print 'done'

if __name__ == '__main__':
    main()
