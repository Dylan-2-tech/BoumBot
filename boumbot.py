import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
chrome.get('https://jklm.fun/CGAD')

time.sleep(2)

try:
	nickName = chrome.find_element(By.CLASS_NAME,'styled')
	nickName.clear()
	nickName.send_keys("BoomBot")
	nickName.send_keys(Keys.RETURN)
except Exception:
	print("Can't register as BoomBot")

time.sleep(5)

try:
	joinGame = chrome.find_element(By.TAG_NAME,'button')
	joinGame.click()
except Exception:
	print("Cannot join the game")

time.sleep(5)


"""



try:
	gameType = chrome.find_element(By.CLASS_NAME,"styled")
	gameType.click()
except Exception:
	print("cannot find the BombParty type")

time.sleep(5)




try:
	search.send_keys("Hey, Tecadmin")
	search.send_keys(Keys.RETURN)
except Exception:
	print("You didn't close the google first pop up")


time.sleep(5)
#driver.close()
"""