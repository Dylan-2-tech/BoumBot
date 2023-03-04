import json

# Function that return true if the word was already given and false otherwise
def word_already_given(word,lowag):

    indWord = 0 # index that refer the word in lowag
    exist = False # boolean to confirm if the word was already given
    while indWord < len(lowag) and not exist: # while we haven't check all the words and not found a word that already exist
        exist = word == lowag[indWord] # if the word search is present, exist is True and False othewise
        indWord += 1 # increment to check the next word

    return exist


# Function that return the word who was not already given with the syllables asks into it 
def first_word(listOfWord,LowAlreadyGiven,syllable):
    """Sequential search"""    

    found = False # boolean to check if we have found the word
    indWord = 0 # index that refer the word in listOfWord
    lenLOW = len(listOfWord) # length of the listOfWord

    while not found and indWord < lenLOW: # while we haven't found the word and we aren't at the end of the listOfWord
        found = syllable in listOfWord[indWord] # if the syllable searched is present in the word found is True and False otherwise
        if found and word_already_given(listOfWord[indWord],LowAlreadyGiven): # if the word is found and already given
            found = False # we haven't found the right one
        indWord += 1 # increment to check the next one

    LowAlreadyGiven.append(listOfWord[indWord-1]) # append the word found to the lowag list
    return listOfWord[indWord-1] # returns the word


# return True if the word is found in the vocabullary.json and false otherwise
def search_word_json(vocabullary,syllable,lowag):

    indWord = 0 # index to refer the word
    if syllable in vocabullary.keys(): # if the syllable is contain in the vocabullary
        while indWord < len(vocabullary[syllable]): # while 
            word = vocabullary[syllable][indWord] # word is equal to the word at the index indWord
            if not word_already_given(word, lowag): # if the word the word is not already given
                return word # we return the word
            indWord += 1 # else we compare to the next word
    return False # we return False if we have found it or not


# Returns the index of the word who contains the syllable searched
def first_ind_syllable(listOfWord,syllable):
    """binary search"""

    start = 0 # start value for the binary search
    end = len(listOfWord) - 1 # end value for the binary search
    found = False # boolean to confirm if we have found the word

    while not found and start <= end: # while we haven't found the word and we haven't parse all the words
        mid = (start+end) // 2 # mid is the index of the word at the middle of the list

        if syllable in listOfWord[mid]: # if the syllable searched is present in the word 
            if mid > 0 and syllable in listOfWord[mid-1]: # if the syllable is present to in the word before 
                end = mid - 1 # the end is equal to mid - 1
            else: # if the syllable is not in the word before, we have found the right one
                found = True
                indWord = mid # the index of the word is mid
        elif syllable < listOfWord[mid]: # if the syllable seems to appear into words below the middle one
            end = mid - 1 
        else:
            start = mid + 1

    if start > end: # if we don't have found the word
        return len(listOfWord)-1 #we return the index of the '###' tag

    return indWord # it return the indWord if we have found it