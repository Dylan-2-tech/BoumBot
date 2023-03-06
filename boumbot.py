import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import ttk
import json
import SearchWords as sw
import DataCreator as dc
from json.decoder import JSONDecodeError


# function that will launch the game
def launch_game():

	print("\n\nStart of the party !")

	dc.clean_vocabulary("DataFolder/liste_francais.txt")

	userName = userName_entry.get()
	if userName == "":
		userName = "BoumBot"
	code = entry_code.get() # We retrieve the code who is in the entry
	# Check if the code is correct
	if len(code) != 4: # If the code length is not 4 characters so it's a wrong code
		# Display of the error label
		wrongLabel = Label(boumWindow,text = "You have entered a wrong party code (EX: ABCD).",bg="#403831",font=("Arial",10),fg="red")
		wrongLabel.pack(side="top")
		wrongLabel.after(2000,wrongLabel.destroy) # destroying label after 2 seconds of display
		return -1

	options = Options()
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	 
	# Chrome webpage launch with the url, /!\ IF THE CODE IS FOR AN OLD PARTY THE ERROR WILL BE SPOTTED AT LINE 101--------------------------------
	chrome.get(f'https://jklm.fun/{code}') 
	

	# Step of connecting the bot with the username used in line 42
	try:
		# Implicit wait for the username input appear on the webpage
		uN = WebDriverWait(chrome, 60).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.pages > div.setNickname.page > form > div.line > input"))
		)
		uN.clear() # We clear because there is a default guest username
		uN.send_keys(userName) # UserName, DEFAULT='BoomBot' if the entry is empty
		uN.send_keys(Keys.RETURN) # Return the nickname to the webpage

	except ElementNotInteractableException: # Excetion if the program has not found the input
		print("input not found")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "Input not found, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		chrome.close() # Closing chrome
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		return -1 # we return -1 to stop the program

	# Step to check if the page loads correctly
	try:
		# Implicit wait for those who have bad connection
		game = WebDriverWait(chrome, 10).until( # Wait 10 seconds until...
			EC.presence_of_element_located((By.CLASS_NAME, "game")) # ... the game div is located (The page has load correctly)
		)
		print("load correctly") 

	except NoSuchElementException: # Exception if the page took to long to load
		print("too long to load")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "The page took to long to load, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		chrome.close() # Closing chrome
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		return -1 # we return -1 to stop the program

	time.sleep(1) # Sleep to wait for the page to load

	"""
	The BombParty game hapens in an iframe which is located differently from the main page of the website.
	To locate element from the Iframe I have to switch to webpage we want to locate element on.

	I have to first locate the Iframe then to switch.
	"""
	try:
		# Implicit wait for those who have bad connection
		iframe = WebDriverWait(chrome, 60).until( # Wait 1 minute until ...
			EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div[1]/iframe')) # ... the iframe has load correctly
		)
		chrome.switch_to.frame(iframe) # Switching to the Iframe
		print("Iframe found")
		# NOW ALL THE ELEMENT LOCATED ARE IN THE IFRAME AND NOT IN THE MAIN WEBPAGE ANYMORE
		
	except NoSuchElementException: # THIS ERROR HAPPEN WHEN THE CODE OF THE PARTY IS FOR AN OLD PARTY OR WHEN THE CODE IS WRONG
		print("old party")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "The code you have entered is for an old party or a wrong one, please try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		return -1 # we return -1 to stop the program


	try:
		# Implicit wait for those who have bad connection
		join = WebDriverWait(chrome, 60).until( # Wait 1 minute until ...
			EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[1]/button")) # ... the button is on the webpage
		)
		time.sleep(1)
		join.click() # When the button is clickable, we click

	except NoSuchElementException: # exception if the program has not find the join button
		print("join not found")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "join button not found, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)  # Destroying the label after 5 seconds of display
		chrome.close() # Closing chrome
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exeption if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		return -1 # we return -1 to stop the program


	try:
		# Implicit wait for those who have bad connection
		syllableDiv = WebDriverWait(chrome, 60).until( # wait 1 minute until ...
			EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div')) # ... the div with the syllable appear
		)
	except NoSuchElementException: # Excpetion if the page took to long to load
		print("cant find the syllable")
		# Display of the error label
		ERRORLabel = Label(boumWindow,text = "Can't find the syllable, may try again with a better connection.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
		chrome.close() # Closing chrome
		return -1 # we return -1 to stop the program

	# We locate the input where the word needs to be entered 
	say = chrome.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

	# We open the txt files who contains the list of words
	with open("DataFolder/liste_francais.txt","r",encoding = "latin-1") as f:
		words = [line.strip() for line in f]
	f.close() # Closing the txt file

	# we open the json file that contain the data (vocabulary)
	with open("DataFolder/vocabulary.json", "r") as j: # opening the file
		try: # We need to try because if the vocabulary.json file is empty it returns the 'JSODecodeError' error
			vocabulary = json.load(j) # loading all the data of the vocabulary
		except JSONDecodeError: # Error if the vocabulary file is empty
			vocabulary = False # Vocaullary is False (needed for line 203)
	j.close() # Closing the Json file

	lowag = [] # this is the list of word that are already given
	newSyllable = [] # list of the new syllable to learn

	nbrWordVoc = 0 # the number of word give thanks to the vocabulary
	nbrWordNotVoc = 0 # the number of word give thanks to the sequential search

	# We locate the winner div
	winnerDiv = chrome.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div/div[2]")

	while not winnerDiv.is_displayed(): # While the winner is not displayed we continue
		try:
			if say.is_displayed(): # if its True it means that its the turn of the bot to play otherwise if its false
				# Location of the Div where the syllable is
				syllable = chrome.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div').text
				syllable = syllable.lower()

				# When we have the syllable, we search a word in the vocabulary first (it's quicker)
				if type(vocabulary) == dict: # if the vocabulary is False, the word is False too
					word = sw.search_word_json(vocabulary,syllable,lowag) # If the syllable is known in the vocabulary, it returns a word otherwise it return False 
				else:
					word = False # Word is False because the word is not in the vocabulary (go to 209)
					
				if not word: # if word == False we search the word by a sequential search and not thanks to the vocabulary
					print("WORD NOT IN vocabulary")
					newSyllable.append(syllable) # If the syllable is not known, we add it so the bot we learn
					word = sw.first_word(words,lowag,syllable) # The word is the first word that contains the syllable
					nbrWordNotVoc += 1 # incrementing for statistics STONKS
				else:
					print("THE MTHFCKN WORD IS IN THE vocabulary")
					nbrWordVoc += 1 # incrementing for statistics STONKS

				lowag.append(word) # we add the word to the list of word already guiven so we never send the same word
				say.send_keys(word) # We send the word that we found
				say.send_keys(Keys.RETURN)  # We return it
				print("It sends the word", word)
			
			else: # It's the turn of the opponent
				syllable = chrome.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div').text
				syllable = syllable.lower()

				if syllable not in vocabulary.keys():
					newSyllable.append(syllable)
				print("It's not the turn of the bot")

		except ElementNotInteractableException: # If an element of the webpage is not interactable
			print("Error because of bad connection maybe")
			# Display of the error label
			ERRORLabel = Label(boumWindow,text = "Try again with a better connection, it might help",bg="#403831",font=("Arial",10),fg="red")
			ERRORLabel.pack(side="top")
			ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
			return -1 # we return -1 to stop the program

		except NoSuchWindowException: # Exeption if the player has closed the window
			print("window closed")
			# Display of the error label
			ERRORLabel = Label(boumWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
			ERRORLabel.pack(side="top")
			ERRORLabel.after(5000,ERRORLabel.destroy) # Destroying the label after 5 seconds of display
			return -1 # we return -1 to stop the program

		time.sleep(2) # We wait 2 second between each word 

	# get the name of the winner
	winner = chrome.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div/div[2]").text

	if winner == userName: # if the winner is the main player (the bot) we display congrats :)
		WINNERLabel = Label(boumWindow,text = f"Congratulations, you have won :)",bg="green",font=("Arial",14),fg="white")
		WINNERLabel.pack(side="top")
		WINNERLabel.after(5000,WINNERLabel.destroy) # Destroying the label after 5 seconds of display
	else: # If the winner is not the main player (the bot)
		WINNERLabel = Label(boumWindow,text = f"Oh nooo... you have lost :(",bg="red",font=("Arial",14),fg="white")
		WINNERLabel.pack(side="top")
		WINNERLabel.after(5000,WINNERLabel.destroy) # Destroying the label after 5 seconds of display
	
	print(f"\n\nSTATISTICS:\n{nbrWordVoc} words were in the vocabulary")
	print(f"{nbrWordNotVoc} words were not in the vocabulary")

	print("\nEnd of the bot\nStarting of the learning...")

	# Step of learning the words that are not in the vocabulary

	sylWithoutWords = [] # list of syllables without words
	newvocabulary = {} # dictionnary that represent the new vocabulary

	# Creating the vocabulary thanks to a binary search ( very quick but don't get a vocabulary for all words )
	dc.create_dic_word_list_by_syllable(newSyllable,words,newvocabulary,sylWithoutWords)
	# Creating the rest of the vocabulary thanks to a sequential search with the rest of the syllable ( slow but it sure to obtain a vocabulary for all syllable)
	dc.create_dic_word_list_by_syllable_sequential(words,sylWithoutWords,newvocabulary)
	# Append the vocabulary created before to the definitive vocabulary file
	dc.vocabulary_update(newvocabulary,"DataFolder/vocabulary.json")
	

# Tkinter part
# Creation of the main game page
boumWindow = Tk()
boumWindow.title("BoumWindow")
boumWindow.geometry("500x400")
boumWindow["bg"] = "#403831"

# Creation of the title label  
title = Label(boumWindow,text="Let's use BoumBot!",bg="#403831",font=("Arial",25),fg="white")
title.pack(pady=40)

# Creation of the label on top of the entry
entry_label = Label(boumWindow,text="Enter the code party",bg="#403831",font=("Arial",12),fg="white")
entry_label.pack()
# Creation of the entry
entry_code = Entry(boumWindow)
entry_code.pack()

# Creation of the userName label
userName_label = Label(boumWindow,text="What's your userName", bg="#403831",font=("Arial",12),fg="white")
userName_label.pack()

# Creation of the username Entry
userName_entry = Entry(boumWindow)
userName_entry.pack()


# Creation of the button that will launch the game
btnGetCode = Button(boumWindow,text="Get started !",command = launch_game)
btnGetCode.pack(pady=30)

# Creation du bouton pour quitter
btnQuit = Button(boumWindow,text="CLOSE", command = boumWindow.destroy)
btnQuit.pack(pady=20)

boumWindow.mainloop()