import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
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
	c = entry_code.get()
	options = Options()
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	 
	chrome.get(f'https://jklm.fun/{c}')

	time.sleep(2)

	try:
		nickName = chrome.find_element(By.XPATH,'/html/body/div[2]/div[3]/form/div[2]/input')
		nickName.clear()
		nickName.send_keys("BoomBot")
		nickName.send_keys(Keys.RETURN)
	except Exception:
		print("Can't register as BoomBot")

	time.sleep(5)

	try:
		elem = WebDriverWait(chrome, 10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "game"))
		)
	except NoSuchElementException:
		print("Cant find this shit")
	except NoSuchWindowException:
		print("You have closed the window piece of shit")
	
	actions = ActionChains(chrome)
	actions.send_keys(Keys.TAB * 2)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	
	time.sleep(30)
	
	syllabe = chrome.find_element(By.XPATH, './html/body/div[2]/div[2]/div[2]/div[2]/div')
	syllabe.getText()

	"""
	try:
		textAsk = WebDriverWait(chrome, 60).until(
		EC.presence_of_element_located((By.CSS_SELECTOR,'input.styled'))
		)
		dire = ActionChains(chrome)
		dire.send_keys("Behe jtai niqué fdp")
		dire.send_keys(Keys.RETURN)
		dire.perform()
		print("It works")

	except NoSuchElementException:
		print("cant say behe fdp")
		chrome.close()
	except NoSuchWindowException:
		print("You have closed the window piece of shit")


	time.sleep(10)
	"""



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



