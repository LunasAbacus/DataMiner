DataMiner
=========

Authors
=======
Nathan Jacobs
Joshua Adams

Mine all the data, for homework and science!

Files
=====

TagExtractor.py - data structure used to extract tags from the .sgm files that are used to create the feature vectors

stopwords.txt - is a list of stop words that are elimated in a preliminary step when creating a feature vector

FeatureVector2.py - constructs a feature vector for each reuter in the file by pulling out all of the nouns in the body
 
FeatureVector3.py - constructors a feature vector by keeps a count of words that are not listed in stopwords.txt

FeatureVector4.py - constructs a feature vector for each reuter by finding the frequency distribution for each word in the body

output-FeatureVector2.txt - sample output for FeatureVector2

output-FeatureVector3.txt - sample output for FeatureVector3

output-FeatureVector4.txt - sample output for FeatureVector4

Installation
============

Runing The Program
==================

To run the program type 'python FeatureVector[number].py' in terminal
where number is the feature vector that is being run

The output for each program will be according to the number of the feature
vector that is executed. For example FeatureVector2.py will create the file
'output-FeatureVector2.txt' which is the output file for FeatureVector2.

