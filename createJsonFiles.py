import json

def no_accent_char(char):
    """Retire l'accent d'un caractère"""
    table_correspondance = {192 : 65,
                            193 : 65,
                            194 : 65,
                            195 : 65,
                            196 : 65,
                            197 : 65,
                            198 : 65,
                            199 : 67,
                            200 : 69,
                            201 : 69,
                            202 : 69,
                            203 : 69,
                            204 : 73,
                            205 : 73,
                            206 : 73,
                            207 : 73,
                            208 : 68,
                            209 : 78,
                            210 : 79,
                            211 : 79,
                            212 : 79,
                            213 : 79,
                            214 : 79,
                            216 : 79,
                            217 : 85,
                            218 : 85,
                            219 : 85,
                            220 : 85,
                            221 : 89,
                            224 : 97,
                            225 : 97,
                            226 : 97,
                            227 : 97,
                            228 : 97,
                            229 : 97,
                            230 : 97,
                            231 : 99,
                            232 : 101,
                            233 : 101,
                            234 : 101,
                            235 : 101,
                            236 : 105,
                            237 : 105,
                            238 : 105,
                            239 : 105,
                            240 : 111,
                            241 : 110,
                            242 : 111,
                            243 : 111,
                            244 : 111,
                            245 : 111,
                            246 : 111,
                            248 : 111,
                            249 : 117,
                            250 : 117,
                            251 : 117,
                            252 : 117,
                            253 : 121
                            
        
    }

    if 192 <= ord(char) <= 214 or 216 <= ord(char) <= 253:
        return chr(table_correspondance[ord(char)])
    else:
        return char

    return new_string


def no_accent_word(string):
    """Retire tous les accents d'un mot"""
    new_string = ""
    for char in string:
        new_string += no_accent_char(char)

    return new_string


def create_json(data,filename):
	with open(filename,"w") as f:
		json.dump(data,f,indent=2)

def read_json(filename):
	with open(filename,"r") as f:
		data = json.load(f)
		print(data["en"])

lowag = []

def word_already_given(word,lowag):
    
    for i in range(len(lowag)):
        if lowag[i] == word:
            return True

    return False

def first_sequentielle(list_of_word,LOW_already_given,syllable):

    found = False
    ind = 0
    lenLOW = len(list_of_word)

    while not found and ind < lenLOW:
        found = syllable in list_of_word[ind]
        if found and word_already_given(list_of_word[ind],LOW_already_given):
            found = False
        ind += 1

    LOW_already_given.append(list_of_word[ind-1])
    return list_of_word[ind-1]


with open("liste_francais.txt", "r") as f:
    words = [line.strip() for line in f]

with open("syllabes.txt", "r") as f:
    syllables = [line.strip() for line in f]

for i in range(len(syllables)):
    print(first_sequentielle(words,lowag,syllables[i]), " syllable = ", syllables[i])


def first_ind_syllable(list_of_word,syllable):
	start = 0
	end = len(list_of_word) - 1
	found = False

	while not found and start <= end:
		mid = (start+end) // 2

		if syllable in no_accent_word(list_of_word[mid].strip().lower()):
			if mid > 0 and syllable in no_accent_word(list_of_word[mid-1].strip().lower()):
				end = mid - 1
			else:
				found = True
				ind = mid
		elif syllable < no_accent_word(list_of_word[mid].strip().lower()):
			end = mid - 1
		else:
			start = mid + 1

	if start > end:
		#print(len(list_of_word)-1)
		return len(list_of_word)-1

	return ind

dic = {}
syllableWithoutWord = []

def create_dic_word_list_by_syllable(syllableList,wordListfile,dic):
	
	with open(syllableList) as s:# We open the syllable list file
		with open(wordListfile) as w: # We open the file with the word list

			# We initialize those two variables to enter the while loops
			syllable = s.readline().lower().strip()

			indWord = 0

			listOfWord = w.readlines()

			while syllable != "endoffile": # while we're not at the end of the file
				syllable = s.readline().lower().strip() # we clear the syllable and remove the '\n'
				if syllable not in dic.keys(): # If the syllable has still no words
					dic[syllable] = [] # We initialize an empty tab that will contains the words
				#print("changement ---------------- nouvelle syllabe: ", syllable)

				indWord = first_ind_syllable(listOfWord,syllable)
				#print("Premier mot qui contient :", syllable, " est ", listOfWord[indWord])
				while len(dic[syllable]) != 20 : # While the syllable don't have a list of 20 words #and word != ""
					word = no_accent_word(listOfWord[indWord].lower().strip())# we set the varaible 'word' with a word in the list at the index 'indWord' and strip() to remove the white spaces
					if word == "endoffile":

						break
					elif syllable in word: # If the syllable is in the word
						dic[syllable].append(word) # We add it into the list of words
					indWord += 1
					#print(len(dic[syllable]),syllable, word)


#create_dic_word_list_by_syllable("syllabes.txt","liste_francais.txt",dic)
#create_json(dic,"test.json")


# FIRST IND SYLLABE BUT MODIFIED TO RETURN DIRECTLY THE WORD
def search_word(list_of_word,syllable):
    start = 0
    end = len(list_of_word) - 1
    found = False

    while not found and start <= end:
        mid = (start+end) // 2

        if syllable in no_accent_word(list_of_word[mid].strip().lower()):
            if mid > 0 and syllable in no_accent_word(list_of_word[mid-1].strip().lower()):
                end = mid - 1
            else:
                found = True
        elif syllable < no_accent_word(list_of_word[mid].strip().lower()):
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        return "not found"

    return no_accent_word(list_of_word[mid].strip().lower())

"""
with open("test.json") as j:
    data = json.load(j)


def create_txt(data):
    with open("syllabes.txt","w") as f:
        for k in data.keys():
            f.write(k+"\n")


create_txt(data)


with open("../liste_francais.txt") as f:
    data = f.readlines()
    print(search_word(data,"a"))


# Open file    
fileHandler = open ("liste_francais.txt", "r")
# Get list of all lines in file
listOfLines = fileHandler.readlines()
# Close file 
fileHandler.close()
# Iterate over the lines
for line in listOfLines:
	l = line.strip()
	if l == "END":
   		print("fin")



with open("liste_francais.txt") as f:
    mots = f.readlines()
    ind = first_ind_syllable(mots,"qu")
    if ind > 0:
        motavant = mots[ind-1]
    else:
        motavant = "Debut du fichier"
    mot = mots[ind]
    print("motavant: ",motavant, "\n", mot)


if "uoi" > "quo":
	print("Vrai")
else:
	print("False")
"""

"""
# PARTIE SUR LA RECHERCHE -----------------------------------
def word(file,syllable):
    with open(file) as f:
        data = json.load(f)
        return data[syllable][ind]

word("test.json",0)
"""