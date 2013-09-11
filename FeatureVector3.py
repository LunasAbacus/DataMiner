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
import re
import sys

def AddToDict(daDic, word, blacklist):
    if (len(word) > 2) and (word not in blacklist):
        if word in daDic:
            daDic[word] += 1
        else:
            daDic[word] = 1

def main():
    articleMap = {}
    blacklist = []

    #todo - use stop word found at
    #http://www.webconfs.com/stop-words.php
    #alread created file just read it
    with open('stopwords.txt') as f:
        for line in f:
            blacklist.append(line.rstrip())

    print "printing first " + str(sys.argv[1]) + "sgm files"

    with open('output.txt','w') as wr:
        #for i in range(0,23):
        for i in range(0,sys.argv[1]):
            filename = "reut2-%s.sgm" % ("%03d" % i)
            print filename
            sgm = RR(filename)
            for j in range(0,sgm.NumberOfReuters()-1):
            #for j in range(0,1):
                article = {}
                title = sgm.ExtractTagData(j,"TITLE")
                #print title
                wr.write("\n"+title)
                body = sgm.ExtractTagData(j,"BODY")
                body = re.sub("[\d]"," ", body)
                body = re.sub("[^\w]"," ", body)
                body = body.lower()
                for token in body.split():
                    #print token
                    AddToDict(article, token, blacklist)
                for key in sorted(article.keys()):
                    #print key + ":" + str(article[key])
                    wr.write("\n\t" + key + ":" + str(article[key]))
                articleMap[title] = article
            #print articleMap
        print 'done'

if __name__ == '__main__':
    main()
