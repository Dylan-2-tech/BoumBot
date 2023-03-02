import json

# Function that return true if the word was already given and false otherwise
def word_already_given(word,lowag):

    ind = 0
    exist = False
    while ind < len(lowag) and not exist:
        exist = word == lowag[ind]
        ind += 1

    return exist


# Function that return the word who was not already given with the syllables asks into it 
def first_word(listOfWord,LowAlreadyGiven,syllable):
    """Sequential search"""    

    found = False
    ind = 0
    lenLOW = len(listOfWord)

    while not found and ind < lenLOW:
        found = syllable in listOfWord[ind]
        if found and word_already_given(listOfWord[ind],LowAlreadyGiven):
            found = False
        ind += 1

    LowAlreadyGiven.append(listOfWord[ind-1])
    return listOfWord[ind-1]


# return True if the word is found in the vocabullary.json and false otherwise
def search_word_json(filename,syllable,lowag,dic):

    ind = 0
    found = False
    with open(filename,"r") as j:
        data = json.load(j)
        if syllable in data.keys():
            while ind < len(dic[syllable]) and not found:
                word = dic[syllable][ind]
                if not word_already_given(word, lowag):
                    return word
                ind+=1
    return found



# Returns the index of the word who contains the syllable searched
def first_ind_syllable(listOfWord,syllable):
    """binary search"""

    start = 0
    end = len(listOfWord) - 1
    found = False

    while not found and start <= end:
        mid = (start+end) // 2

        if syllable in listOfWord[mid]:
            if mid > 0 and syllable in listOfWord[mid-1]:
                end = mid - 1
            else:
                found = True
                ind = mid
        elif syllable < listOfWord[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        return len(listOfWord)-1

    return ind