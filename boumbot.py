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


# Function that return the word entered in args without any accent
def no_accent_char(char):
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

# Function that return true if the word was already given and false otherwise
def word_already_given(word,lowag):
    
    for i in range(len(lowag)):
        if lowag[i] == word:
            return True

    return False

# Function that return the word with the syllables asks into it
def first_word(list_of_word,LOW_already_given,syllable):

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


# function that will launch the game
def launch_game():
	code = entry_code.get() # We retrieve the code who is in the entry
	# Check if the code is correct
	if len(code) != 4: # If the code length is not 4 characters so it's a wrong code
		# Display of the error label
		wrongLabel = Label(boomWindow,text = "You have entered a wrong party code (EX: ABCD).",bg="#403831",font=("Arial",10),fg="red")
		wrongLabel.pack(side="top")
		wrongLabel.after(2000,wrongLabel.destroy)
		return -1

	options = Options()
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	 
	# Chrome webpage launch with the url, /!\ IF THE CODE IS FOR AN OLD PARTY THE ERROR WILL BE SPOTTED AT LINE 101--------------------------------
	chrome.get(f'https://jklm.fun/{code}') 
	
	time.sleep(1)

	# Step of connecting the bot with the username used in line 42
	try:
		# Implicit wait for the username input appear on the webpage
		nickName = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.pages > div.setNickname.page > form > div.line > input"))
		)
		nickName.clear() # We clear because there is a default guest username
		nickName.send_keys("BoomBot") # UserName, DEFAULT='BoomBot', /!\ CAN BE CHANGE IF YOU WANT
		nickName.send_keys(Keys.RETURN)

	except ElementNotInteractableException: # Excetion if the program has not found the input
		print("input not found")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "Input not found, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		chrome.close()
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program

	# Step to check if the page loads correctly
	try:
		# Implicit wait for those who have bad connection
		game = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "game"))
		)
		print("load correctly") # Confirmation de la présence de la div game

	except NoSuchElementException: # Exception if the page took to long to load
		print("too long to load")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "The page took to long to load, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		chrome.close()
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program


	time.sleep(2)
	"""
	The BombParty game hapens in an iframe which is located differently from the main page of the website.
	To locate element from the Iframe I have to switch to webpage we want to locate element on.

	I have to first locate the Iframe then to switch.
	"""
	try:
		iframe = chrome.find_element(By.XPATH,'/html/body/div[2]/div[4]/div[1]/iframe')
		chrome.switch_to.frame(iframe) # Switching
		print("Iframe found")
		# NOW ALL THE ELEMENT LOCATED ARE IN THE IFRAME AND NOT IN THE MAIN WEBPAGE ANYMORE
		
	except NoSuchElementException: # THIS ERROR HAPPEN WHEN THE CODE OF THE PARTY IS FOR AN OLD PARTY
		print("old party")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "The code you have entered is for an old party, please try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exception if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program

	time.sleep(2) # waiting for thos who have bad connection

	# If the page load correctly, we join the game
	try:
		# Implicit wait for those who have bad connection
		join = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[1]/button"))
		)
		join.click() # When found We click on the button to join

	except NoSuchElementException: # exception if the program has not find the join button
		print("join not found")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "join button not found, try again.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		chrome.close()
		return -1 # we return -1 to stop the program

	except NoSuchWindowException: # Exeption if the player has closed the window
		print("window closed")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program

	# We search the input where the word needs to be entered 
	say = chrome.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

	# We open the txt files who contains the list of words
	with open("liste_francais.txt") as f:
		words = [line.strip() for line in f]

	# We locate the winner div
	winnerDiv = chrome.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[3]/div/div[2]")

	try:
		start = WebDriverWait(chrome, 60).until(
			EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div'))
		)
	except NoSuchElementException:
		print("cant find the syllable")
		# Display of the error label
		ERRORLabel = Label(boomWindow,text = "Can't find the syllable.",bg="#403831",font=("Arial",10),fg="red")
		ERRORLabel.pack(side="top")
		ERRORLabel.after(5000,ERRORLabel.destroy)
		return -1 # we return -1 to stop the program
	
	lowag = [] # this is the list of word that are already given

	winner = False # boolean to enter the loop
	while not winner: # While the winner is not displayed we continue
		try:
			if say.is_displayed(): # if its True it means that its the turn of the bot to play otherwise if its false
				# Location of the Div where the syllable is
				syllable = chrome.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div').text
				syllable = syllable.lower()

				# When we have the syllable, we send it to the webpage
				word = first_word(words,lowag,syllable)
				lowag.append(word) # we add the word to the list of word already guiven so we never send the same word
				say.send_keys(word) # We send the word that we found
				say.send_keys(Keys.RETURN)  # We return it
				print("It sends the word", word)
			
			else:
				print("It's not the turn of the bot")
				winner = winnerDiv.is_displayed()

		except ElementNotInteractableException:
			print("to long to start")
			# Display of the error label
			ERRORLabel = Label(boomWindow,text = "The game took to long to start, try again when someone is waiting.",bg="#403831",font=("Arial",10),fg="red")
			ERRORLabel.pack(side="top")
			ERRORLabel.after(5000,ERRORLabel.destroy)
			return -1 # we return -1 to stop the program

		except NoSuchWindowException: # Exeption if the player has closed the window
			print("window closed")
			# Display of the error label
			ERRORLabel = Label(boomWindow,text = "You have closed the window.",bg="#403831",font=("Arial",10),fg="red")
			ERRORLabel.pack(side="top")
			ERRORLabel.after(5000,ERRORLabel.destroy)
			return -1 # we return -1 to stop the program

		time.sleep(2) # We wait 2 second between each word 
	print("End of the program")
	f.close()


# Tkinter part
# Creation of the main game page
boomWindow = Tk()
boomWindow.title("BoumWindow")
boomWindow.geometry("500x400")
boomWindow["bg"] = "#403831"

# Creation of the title label  
title = Label(boomWindow,text="Let's use BoomBot!",bg="#403831",font=("Arial",25),fg="white")
title.pack(pady=40)

# Creation of the label on top of the entry
entry_label = Label(boomWindow,text="Enter the code",bg="#403831",font=("Arial",15),fg="white")
entry_label.pack()
# Creation of the entry
entry_code = Entry(boomWindow)
entry_code.pack()

# Creation of the button that will launch the game
btnGetCode = Button(boomWindow,text="Get started !",command = launch_game)
btnGetCode.pack(pady=30)

# Creation du bouton pour quitter
btnQuit = Button(boomWindow,text="CLOSE", command = boomWindow.destroy)
btnQuit.pack(pady=20)

boomWindow.mainloop()