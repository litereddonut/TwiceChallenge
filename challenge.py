#!/usr/bin/python

#
# Author: Kevin Ho; kevinchiho@gmail.com
#

import sys

dict = []

def wordJumb(currLetters, remainingWord):
    currentWords = []
    
    if currLetters in dict:
        #if the current letters we were passed are a word in our dictionary add it to our list of working words
        currentWords.append(currLetters)
    
    #for the unused letters, append them to the currLetters we have and pass them recursively to wordJumb, wordJumb will see if this new word is applicable
    for index, x in enumerate(remainingWord):
        newRemaining = remainingWord[:index] + remainingWord[index+1:]
        
        #if we already have the currLetters+x in the currentWords list, we have already gone down that road, do not repeat work
        if currLetters+x not in currentWords:
            nextJumble = wordJumb( (currLetters+x) , newRemaining )
            if ( len(nextJumble) > 0 ):
                #get the union, as we may have duplicates
                currentWords = list( set(currentWords) | set(nextJumble) )
        
    return currentWords

def main(argv):
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        sys.exit('Usage: %s "word to unjumble" "filepath to dictionary"' % sys.argv[0])

    #bring in the dictionary for comparison
    #depending on how big the dictionary is, having it all in memory may not be feasible
    #also depending on the size of the word passed in and the size of the dictionary, may be more efficient to run a binary search for each lookup in wordJumb
    with open(sys.argv[2]) as file:
        for line in file:
            dict.append( line.replace("\n", "") )
            
    words = wordJumb("", sys.argv[1])
    print words
    pass

if __name__ == "__main__":
    main(sys.argv)