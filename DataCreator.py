import json
import SearchWords as sw
import unicodedata

# Create a json file using a dictionnary (data) and a filename
def create_vocabullary(data,filename):
	with open(filename,"w") as f:
		json.dump(data,f,indent=2)
	print("vocabullary learned !")

# Read the json and display the json file using his name file
def read_json(filename):
	with open(filename,"r") as j:
		data = json.load(j)
		for syllable, word in data.items():
			print(f"{syllable} : {word}\n")


# Create a dictionnary with the syllable as keys and a list of words as values
def create_dic_word_list_by_syllable(listOfSyllable,listOfWord,dic,sylwoW):

	lenWord = len(listOfWord) # the length of the list of words
	indSyl = 0
	while indSyl < len(listOfSyllable): # while we're not at the end of the syllable list
		syllable = listOfSyllable[indSyl] # The syllable is equal to the syllable at the index 'indSyl'
		if syllable not in dic.keys(): # If the syllable is not in the dictionnary
			dic[syllable] = [] # We initialize an empty tab that will contains the words for the syllable

		indWord = sw.first_ind_syllable(listOfWord,syllable) # indWord is the index of the first word with the syllable in it that appear in the list
		while len(dic[syllable]) != 20 : # While the syllable don't have a list of 20 words
			word = listOfWord[indWord-1] # the word is equal to the word at the index 'indWord'
			if indWord == lenWord: # If we are at the end of the list of words
				sylwoW.append(syllable) # we append the syllable in a list of syllable without words 
				dic.pop(syllable) # We remove the syllable from the dictionnary
				break # then we leave this loop because we are at the end of the list of words
			elif syllable in word: # If the syllable is in the word
				dic[syllable].append(word) # We add it into the list of words

			indWord += 1# we increment to compare to an other word

		indSyl += 1 # we increment to compare to an other syllable


# add in a dictionnary as key a syllable and as value the words that contain the syllable
def create_dic_word_list_by_syllable_sequential(listOfWord,sylwoW,dic):
    """Sequential search"""

    lenWord = len(listOfWord) # the length of the list of words
    indSyl = 0 # index to refer the syllable in the list
    while indSyl < len(sylwoW): # while we're not at the end of the list of syllable
        syllable = sylwoW[indSyl] # The syllable is equal to the syllable at the index 'indSyl'
        if syllable not in dic.keys(): # If the syllable is not in the dictionnary
            dic[syllable] = [] # We initialize an empty tab that will contains the words for the syllable

        indWord = 0 # index to refer the word in the list
        while len(dic[syllable]) != 20: # While a syllable has not 20 words
            word = listOfWord[indWord-1]  # the word is equal to the word at the index 'indWord'
            if indWord == lenWord: # if we are at the end of the list of words
                if len(dic[syllable]) == 0: # if the syllable has 0 words
                    dic.pop(syllable) # We delete the syllable from the dictionnary
                break # then we leave this loop because we are at the end of the list of words
            elif syllable in word: # else if the syllable is contain in the word
               	dic[syllable].append(word) # we add the word to the list of words of the syllable

            indWord += 1 # we increment to compare to an other word

        indSyl += 1 # we increment to compare to an other syllable


# Remove all the accent in a string (not from me)
def remove_accents(string):
    return ''.join(char for char in unicodedata.normalize('NFD', string)
                   if unicodedata.category(char) != 'Mn')

# return True if at the end of the file is written '###' and false otherwise
def is_clean(data):
	"""
	/!\ '###' means that all the words in the file are in lowercase and without any accent
	It's like a certification 
	"""
	if len(data) == 0:
		print("The file is empty")
		return True
	else:
		if data[len(data)-1] == "###":
			return True
		else:
			return False

# Clean the words contain in the file (remove all accent and capital letter)
def clean_vocabullary(filename):
	# Opens the list of words file and create a list with all words in without '\n' or Upper letters
	with open(filename, "r+", encoding = "latin-1") as f:
		words = [word.lower() for word in f]

		if is_clean(words): # if the file is clean
			print("All the words are normalized")

		else: # if the file is not clean
			# clearing the words
			print("clearing the words")
			words = [remove_accents(word) for word in words]
			
			# overwriting the words from the start
			f.seek(0) # /!\ Without the seek to 0 it copy paste the content and rewrite it at the end of the file
			f.writelines(words)
			f.write("\n###")

	f.close() # closing the file



read_json("vocabullary.json")