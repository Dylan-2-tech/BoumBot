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
def search_word_json(vocabullary,syllable,lowag):

    indWord = 0 # index to refer the word
    if syllable in vocabullary.keys(): # if the syllable is contain in the vocabullary
        while indWord < len(vocabullary[syllable]): # while 
            word = vocabullary[syllable][indWord] # word is equal to the word at the index indWord
            if not word_already_given(word, lowag): # if the word the word is not already given
                return word # we return the word
            indWord += 1 # else we compare to the next word
    return False # we return False if we have found it or not

"""
# we open the json file that contain the data (vocabullary)
with open("vocabullary.json","r") as j: # opening the file
    vocabullary = json.load(j) # loading all the data of the vocabullary

word = search_word_json(vocabullary,"a",['aaron', 'abaisse', 'abaissement', 'abaisser', 'abandon', 'abandonnant', 'abandonne', 'abandonne', 'abandonnee', 'abandonnees', 'abandonnent', 'abandonner',  'abasie', 'abasourdi', 'abasourdir', 'abasourdissement', 'abat-jour', 'abats', 'abattage'])

if word:
    print(word)
if not word:
    print("mot pas trouvé")
"""

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