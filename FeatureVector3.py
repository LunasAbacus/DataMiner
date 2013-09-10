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

def AddToDict(daDic, word, blacklist):
    if word not in blacklist and len(word) > 2:
        if word in daDic:
            daDic[word] += 1
        else:
            daDic[word] = 1

def main():
    articleMap = {}


    #todo - use stop word found at
    #http://www.webconfs.com/stop-words.php
    #alread created file just read it
    blacklist = ['also','and','are','the','its']

    #for i in range(0,23):
    for i in range(0,1):
        filename = "reut2-%s.sgm" % ("%03d" % i)
        print filename + "\n"
        sgm = RR(filename)
        #for j in range(0,sgm.NumberOfReuters()-1):
        for j in range(0,1):
            article = {}
            title = sgm.ExtractTagData(j,"TITLE")
            #print title
            body = sgm.ExtractTagData(j,"BODY")
            body = re.sub("[\d]"," ", body)
            body = re.sub("[^\w]"," ", body)
            body = body.lower()
            for token in body.split():
                #print token
                AddToDict(article, token, blacklist)
            for key in sorted(article.keys()):
                print key
            articleMap[title] = article
        #print articleMap
        print 'done'

if __name__ == '__main__':
    main()
