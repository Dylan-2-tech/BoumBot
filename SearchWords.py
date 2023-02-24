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


# Returns the index of the word who contains the syllable searched
def first_ind_syllable(listOfWord,syllable):
	start = 0
	end = len(listOfWord) - 1
	found = False

	while not found and start <= end:
		mid = (start+end) // 2

		if syllable in no_accent_word(listOfWord[mid]):
			if mid > 0 and syllable in no_accent_word(listOfWord[mid-1]):
				end = mid - 1
			else:
				found = True
				ind = mid
		elif syllable < no_accent_word(listOfWord[mid]):
			end = mid - 1
		else:
			start = mid + 1

	if start > end:
		return len(listOfWord)-1

	return ind

# FIRST IND SYLLABE BUT MODIFIED TO RETURN DIRECTLY THE WORD
def search_word(listOfWord,syllable):
    start = 0
    end = len(listOfWord) - 1
    found = False

    while not found and start <= end:
        mid = (start+end) // 2

        if syllable in no_accent_word(listOfWord[mid]):
            if mid > 0 and syllable in no_accent_word(listOfWord[mid-1]):
                end = mid - 1
            else:
                found = True
        elif syllable < no_accent_word(listOfWord[mid]):
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        return False

    return no_accent_word(listOfWord[mid])



# TEST DE WORD_ALREADY_GIVEN

lowag = ["manger", "boire"]

print(word_already_given("boire",lowag))