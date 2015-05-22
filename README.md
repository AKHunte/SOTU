# SOTU
State of the Union Text Mining Project

This project does some basic text mining of State of the Union Addresses.  The programs are written in Python and use Hadoop streaming to calclate the word frequency. The program calculates the average, minimim, and maximum times each word appears. Starting in 1984, the program computes the average and standard deviation of times a word appears in a window of five years.  Using the calculations from the roling 5 year windows, words with a frequency that exceeds the average plus two standard deviations in the year immediately following the window are labeded as trending words.
