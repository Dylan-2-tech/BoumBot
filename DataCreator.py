import json
import SearchWords as sw

# Create a json file using a dictionnary (data) and a filename
def create_json(data,filename):
	with open(filename,"w") as f:
		json.dump(data,f,indent=2)

# Read the json and display the json file using his name file
def read_json(filename):
	with open(filename,"r") as j:
		data = json.load(j)
		for syllable, word in data.items():
			print(f"{syllable} : {word}\n")

# return True if the word is found in the vocabullary.json and false otherwise
def search_word_json(filename,syllable,lowag):
	ind = 0
	with open(filename,"r") as j:
		data = json.load(j)
		if syllable in data.keys():
			while dic[syllable][ind] != sw.word_already_given(syllable[ind], lowag)

# Create a dictionnary with the syllable as keys and a list of words as values
def create_dic_word_list_by_syllable(listOfSyllable,listOfWord,dic):

	indWord = 0
	indSyl = 0

	while listOfSyllable[indSyl] != "endofsyl": # while we're not at the end of the file
		if listOfSyllable[indSyl] not in dic.keys(): # If the syllable has still no words
			dic[listOfSyllable[indSyl]] = [] # We initialize an empty tab that will contains the words
		#print("changement ---------------- nouvelle syllabe: ", syllable)

		indWord = sw.first_ind_syllable(listOfWord,listOfSyllable[indSyl])
		#print("Premier mot qui contient :", syllable, " est ", listOfWord[indWord])
		while len(dic[listOfSyllable[indSyl]]) != 20 : # While the syllable don't have a list of 20 words #and word != ""
			word = sw.no_accent_word(listOfWord[indWord])# we set the varaible 'word' with a word in the list at the index 'indWord' and strip() to remove the white spaces
			if word == "endoffile":
				dic.pop(syllable[indSyl])
				print("Syllable without word")
				break
			elif listOfSyllable[indSyl] in word: # If the syllable is in the word
				dic[listOfSyllable[indSyl]].append(word) # We add it into the list of words
			indWord += 1
			#print(len(dic[syllable]),syllable, word)
		indSyl+=1



syllable = ["a","b","hazu", "endofsyl"]
sylWithoutWords = []

# Opens the list of words file and create a list with all words in without '\n' or Upper letters
with open("liste_francais.txt", "r", encoding = "latin-1") as f:
	words = [line.strip().lower() for line in f]

dic = {}

create_dic_word_list_by_syllable(syllable,words,dic)
print(dic)
#create_json(dic,"vocabullary.json")


#read_json("vocabullary.json")