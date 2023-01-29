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


# function that will launch the game
def launch_game():
	code = entry_code.get() # On récupère le code de la partie que l'on veut rejoindre
	options = Options()
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	 
	chrome.get(f'https://jklm.fun/{code}') # Ouverture d'une page chrome avec l'url de la partie

	# Etape de la connexion du bot avec son pseudo 'BoomBot
	try:
		# On attend jusqu'a que l'input pour rentrer son pseudo apparaisse
		nickName = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/form/div[2]/input'))
		)
		nickName.clear()
		nickName.send_keys("BoomBot") # Pseudo du Bot /!\ Peut être modifié si vous voulez faire une petite blague à vos amis
		nickName.send_keys(Keys.RETURN)
	except ElementNotInteractableException: # Exceptions qui signal si le programme n'à pas réussi à trouver le input 
		print("Cannot find the input")
		chrome.close()
		return -1 # we return -1 to stop the program
	except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre du jeu
		print("You have closed the window")
		return -1 # we return -1 to stop the program

	# Si la page charge correctement alors on poursuis
	try:
		# On attend que la div game (du jeu) arrive pour passer a la suite 
		game = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "game"))
		)
		print("it works, step game div") # Confirmation de la présence de la div game
	except NoSuchElementException: # Esceptions si on ne trouve pas l'élément
		print("Cant find the game div")
		chrome.close()
		return -1 # we return -1 to stop the program
	except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre du jeu
		print("You have closed the window")
		return -1 # we return -1 to stop the program


	time.sleep(2)
	"""
	Comme le Jeu se déroule dans un Iframe, j'ai besoin de switcher 
	la selection des elements sur cet Iframe car ils n'existent pas
	dans le html par défaut.

	Si je fais un chrome.find_element(By.XPATH,'html/body').
	Cela va prendre celui par défaut et pas celui de l'Iframe

	J'ai donc besoin de localiser le Iframe puis de le switch
	"""
	iframe = chrome.find_element(By.XPATH,'/html/body/div[2]/div[4]/div[1]/iframe')
	chrome.switch_to.frame(iframe)

	time.sleep(2)

	# If the page load correctly, we join the game
	try:
		join = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[1]/button"))
		)
		join.click() # We click on the button to join
	except NoSuchElementException:
		print("Cannot find the join Button")
		chrome.close()
		return -1 # we return -1 to stop the program
	except NoSuchWindowException:
		print("You have closed the window")
		return -1 # we return -1 to stop the program

	# Once we have joined the game, we wait for the game to start
	time.sleep(17) # We wait 15sec for the game + 2sec to secure the loading
	
	# While loop that will send the word every 10 seconds
	val = 0
	while val < 12: # It'll loop during 2 mins because it wait 10 sec 12 times => 10*12 = 120s = 2m
		try:
			# localisation de la div syllabe DANS LE IFRAME
			syllabe = chrome.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div').text
			# Action qui va écrire le texte et l'entrer 
			dire = ActionChains(chrome)
			dire.send_keys(syllabe)
			dire.send_keys(Keys.RETURN)
			dire.perform()
			print("It works")
		except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre
			print("You have closed the window")
			return -1 # we return -1 to stop the program

		time.sleep(10) # On attend 10 secondes avant de renvoyer un autre texte
		val += 1 # On incrémente val pour ne pas avoir de boucle infini

# Partie sur tkinter et l'interface qui demande a l'utilisateur le code de la sesssion de jeu (EX: XXXX)
# Creation of the main game page
boomWindow = Tk()
boomWindow.title("BoumWindow")
boomWindow.geometry("500x500")
boomWindow["bg"] = "#403831"

# Creation of the title label  
title = Label(boomWindow,text="Let's use BoomBot!",bg="#403831",font=("Arial",25),fg="white")
title.pack(pady=40)

# Creation of the labelon top of the entry
entry_label = Label(boomWindow,text="Enter the code",bg="#403831",font=("Arial",15),fg="white")
entry_label.pack()
# Creation of the entry
entry_code = Entry(boomWindow)
entry_code.pack()

# Création du bouton qui va lancer le programme
btnGetCode = Button(boomWindow,text="Get started !",command = launch_game)
btnGetCode.pack(pady=30)

# Création du bouton qui ferme la fenetre
btnQuit = Button(boomWindow,text="CLOSE", command = boomWindow.destroy)
btnQuit.pack(pady=100)

boomWindow.mainloop()