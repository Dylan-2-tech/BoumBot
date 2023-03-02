import json
import SearchWords as sw
import unicodedata

# Create a json file using a dictionnary (data) and a filename
def create_vocabullary(data,filename):
	with open(filename,"w") as f:
		json.dump(data,f,indent=2)

# Read the json and display the json file using his name file
def read_json(filename):
	with open(filename,"r") as j:
		data = json.load(j)
		for syllable, word in data.items():
			print(f"{syllable} : {word}\n")


# Create a dictionnary with the syllable as keys and a list of words as values
def create_dic_word_list_by_syllable(listOfSyllable,listOfWord,dic,sylwoW):

	lenWord = len(listOfWord)
	indSyl = 0
	while indSyl < len(listOfSyllable): # while we're not at the end of the file
		syllable = listOfSyllable[indSyl]
		if syllable not in dic.keys(): # If the syllable has still no words
			dic[syllable] = [] # We initialize an empty tab that will contains the words
		#print("changement ---------------- nouvelle syllabe: ", syllable)

		indWord = sw.first_ind_syllable(listOfWord,syllable)
		#print("Premier mot qui contient :", syllable, " est ", listOfWord[indWord])
		while len(dic[syllable]) != 20 : # While the syllable don't have a list of 20 words #and word != ""
			word = listOfWord[indWord-1]# we set the varaible 'word' with a word in the list at the index 'indWord' and strip() to remove the white spaces
			if indWord == lenWord:
				print(f"{syllable} without word")
				sylwoW.append(syllable)
				dic.pop(syllable)
				break
			elif syllable in word: # If the syllable is in the word
				dic[syllable].append(word) # We add it into the list of words
			indWord += 1
			#print(len(dic[syllable]),syllable, word)
		indSyl+=1


# add in a dictionnary as key a syllable and as value the words that contain the syllable
def create_dic_word_list_by_syllable_sequential(listOfWord,sylwoW,dic):
    """Sequential search"""

    lenWord = len(listOfWord)
    indSyl = 0
    while indSyl < len(sylwoW): # while we're not at the end of the file
        syllable = sylwoW[indSyl]
        if syllable not in dic.keys(): # If the syllable has still no words
            dic[syllable] = [] # We initialize an empty tab that will contains the words

        indWord = 0
        while len(dic[syllable]) != 20:
            word = listOfWord[indWord-1]
            if indWord == lenWord:
                if len(dic[syllable]) == 0:
                    dic.pop(syllable)
                else:
                    sylwoW.pop(indSyl)
                break
            elif syllable in word:
                dic[syllable].append(word)
            indWord += 1
        indSyl += 1


# Remove all the accent in a string (not from me)
def remove_accents(string):
    return ''.join(char for char in unicodedata.normalize('NFD', string)
                   if unicodedata.category(char) != 'Mn')

# return True if at the end of the file is written 'is_clean' and false otherwise
def is_clean(data):
	"""
	/!\ is clean means that all the words in the file are in lowercase and without any accent
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
#clean_vocabullary("liste_francais.txt")


dic = {}
syllable = ["a", "b", "ar", "ph", "nne", "uoi", "yiu", "ttr", "po","ffreo"]
sylWithoutWords = []


with open("liste_francais.txt", "r", encoding = "latin-1") as f:
	words = [word.strip() for word in f]

create_dic_word_list_by_syllable(syllable,words,dic,sylWithoutWords)
print("Syllable without words are: ", sylWithoutWords)
create_dic_word_list_by_syllable_sequential(words,sylWithoutWords,dic)
create_vocabullary(dic,"vocabullary.json")
read_json("vocabullary.json")

print("\n les syllabes restantes sont: \n",sylWithoutWords)

