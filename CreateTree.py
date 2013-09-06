import arff
import xml.etree.ElementTree
import re

totstring=""

with open('reut2-000.sgm', 'r') as inF:
    for line in inF:
        string=re.sub("[^0-9a-zA-Z<>/\s=!-\"\"]+","", line)
    totstring+=string


data=xml.etree.ElementTree.fromstring(totstring)

print data

file.close
