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


# Partie sur tkinter et l'interface qui demande a l'utilisateur le code de la sesssion de jeu (XXXX)

# Fonction qui va afficher le code dans la console
def get_code():
	c = entry_code.get() # On récupère le code de la partie que l'on veut rejoindre
	options = Options()
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	 
	chrome.get(f'https://jklm.fun/{c}') # Ouvertur d'une page chrome avec l'url de la partie

	# Etape de la connexion du bot avec son pseudo 'BoomBot
	time.sleep(2) # On attend que la page charge

	try:
		# On attend jusqu'a que l'input pour rentrer son pseudo apparaisse
		nickName = WebDriverWait(chrome, 10).until(
			EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/form/div[2]/input'))
		)
		nickName.clear()
		nickName.send_keys("BoomBot") # Pseudo du Bot /!\ Peut être modifié si vous voulez vous faire passer flash
		nickName.send_keys(Keys.RETURN)
	except ElementNotInteractableException: # Exceptions qui signal si le programme n'à pas réussi à trouver le input 
		print("Je trouve pas le input")
	except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre du jeu
		print("You have closed the window piece of shit")

	# Si la page charge correctement alors on poursuis
	try:
		# On attend que la div game (du jeu) arrive pour passer a la suite 
		game = WebDriverWait(chrome, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "game"))
		)
		print("ya game") # Confirmation de la présence de la div game
	except NoSuchElementException: # Esceptions si on ne trouve pas l'élément
		print("Cant find this shit")
		chrome.close()
	except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre du jeu
		print("You have closed the window piece of shit")
	
	time.sleep(2) # On attend que la page charge.

	# Action qui va faire TAB 2 fois pour aller sur le bouton 'Rejoindre' puis entrer pour rejoindre
	actions = ActionChains(chrome)
	actions.send_keys(Keys.TAB * 2)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	

	time.sleep(17) # On attend le chargement de la partie (15secondes normale + 2secondes de sécurité)
	
	# Collecte de la syllabe 
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
	
	

	# Boucle while qui va toutes les 10 secondes mettre le mot contenant la syllabe recherché
	val = 0
	while val < 12: # On fait la boucle pendant 1 minutes car on met un time sleep de 10 secondes 6 fois
		try:
			# localisation de la div syllabe DANS LE IFRAME
			syllabe = chrome.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div').text
			# Action qui va écrire le texte est l'entré 
			dire = ActionChains(chrome)
			dire.send_keys(syllabe)
			dire.send_keys(Keys.RETURN)
			dire.perform()
			print("It works")
		except NoSuchWindowException: # Exception si le joueur a fermé la fenêtre
			print("You have closed the window piece of shit")
			chrome.close()
		time.sleep(10) # On attend 10 secondes avant de renvoyer un autre texte
		val += 1 # On incrémente val pour ne pas avoir de boucle à l'infini


boumWindow = Tk()
boumWindow.title("BoumWindow")
boumWindow.geometry("500x500")
boumWindow["bg"] = "#403831"

# Création du label de Présentation
label = Label(boumWindow,text="Let's use BoumBot!",bg="#403831",font=("Arial",25),fg="white")
label.pack(pady=40)

# Création de l'entree qui va accueillir le code du jeu
entry_code = Entry(boumWindow)
entry_code.pack(padx=10,pady=30)

# Création du bouton qui va lancer le programme
btnGetCode = Button(boumWindow,text="Go !",command = get_code)
btnGetCode.pack()

# Création du bouton qui ferme la fenetre
btnQuit = Button(boumWindow,text="LEAVE", command = boumWindow.destroy)
btnQuit.pack(pady=100)


boumWindow.mainloop()