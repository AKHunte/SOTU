#!/usr/bin/env python


#Written by: Aisha Hunte
#Date: February 20, 2015

import sys
import os
import string

file_name = os.environ['mapreduce_map_input_file'].split('/')[-1]
file_name = file_name.replace('.txt', '')

dict_word = {}
file_count = os.environ['mapreduce_input_fileinputformat_numinputfiles']
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
	
    #remove the punctuation
    line = line.translate(string.maketrans("",""), string.punctuation)    

    # split the line into words
    words = line.split()
    
    #Output <k,v> = <word,1\sfilename>
    for word in words:
        word = word.strip()
        word = word.lower()
        if word.isdigit():
            continue
        if word in dict_word.keys():
            dict_word[word] +=1
        else:
            dict_word[word] = 1

for key, value in dict_word.iteritems():
    print str(key) + '\t' + str(value) + '\s' + file_name +'\s' + str(file_count)
