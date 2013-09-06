#!/usr/bin/env python

#import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
import re

def ExtractReuters(sgmStr):
    lst = sgmStr.split("<REUTERS")
    return lst[1:] #remove first line which is garbage

def ExtractTagData(reuter, tag):
    #extract data between <Tag>...</Tag>
    startTag = "<"+tag+">"
    endTag = "</"+tag+">"
    startLen = reuter.index(startTag) + len(startTag)
    endLen = reuter.index(endTag)
    return reuter[startLen:endLen]

def ReadSGM(filename):
    #returns an array of reuters for the sgm file
    strList = []

    with open('reut2-000.sgm') as f:
        for line in f:
            line = re.sub("(&#\d+;)","", line)
            line = re.sub("[^\x20-\x7f]+","",line)
            strList.append(line)

    sgm = ''.join(strList)
    return ExtractReuters(sgm)

def main():
    #get a list of reuters
    reuters = ReadSGM('reut2-000.sgm')

    print(ExtractTagData(reuters[0], "BODY"))


if __name__ == '__main__':
    main()
