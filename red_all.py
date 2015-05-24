#!/usr/bin/env python

from operator import itemgetter
import sys
import numpy as np

#Written By: Aisha Hunte
#Date : February 20, 2015
    	
current_count = 0
word = None
current_word = None
current_key = None
current_key_count = 1
year_count = 1
max = 1 
min =1 
dict_words_by_year={}

def avg_sd(w, dict_word):
   years = dict_word.keys()
   sorted_years = sorted(i for i in years if i >= 1984)
   data = np.zeros(5)
   if len(sorted_years) > 0:
       print  'year(s):' , sorted_years
   for i in range(1984, 2010):
       for j in range(0, 4):
           if i+j in sorted_years:
               data[j] = dict_word[i+j]
              #print word, i, dict_word[i]      
       five_avg = data.mean()   
       five_sd = data.std()
       if five_avg != 0:
           print 'years: %d-%d\tavg:%1.2f\tsd:%1.2f' %( i, i+5, five_avg, five_sd)  
           trigger = five_avg + (2*five_sd)
           if i+6 in sorted_years:
       	       if dict_word[i+6] > trigger:
                  print 'TRENDING IN', i+6
   print '------------------------------------------------------------------------------------------------------'
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, value = line.split('\t')
    count, file_name, file_count = value.split('\s')
    year = file_name[:4]
    year = int(year)
    # convert count (currently a string) to int
    try:
        count = float(count)
        file_count = float(file_count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
        dict_words_by_year[year] = count
        if current_year != year:
           year_count += 1
        if count > max:
           max = count
        if count < min:
           min= count
    else:
        if current_word:
            if year_count < file_count:
               min = 0
            # write result to STDOUT
            print '------------------------------------------------------------------------------------------------------'
            print '%s\tavg:%1.2f\tmin:%d\tmax:%d' % (current_word.upper(),float(current_count/file_count), min, max)
            avg_sd(current_word, dict_words_by_year)
        current_count = count
        current_word = word
        current_year = year
        min =1 
        max = 1
        year_count= 1
        dict_words_by_year = {}
# do not forget to output the last word if needed!
if current_word == word:
    if year_count < file_count:
        min = 0
    print '%s\tavg:%1.2f\tmin:%d\tmax:%d' % (current_word.upper(),float(current_count/file_count), min, max)
    print '------------------------------------------------------------------------------------------------------'



     
