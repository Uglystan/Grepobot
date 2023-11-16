from dotenv import load_dotenv
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
load_dotenv()

xpath_table = {
    'logFields': '//input[@id="login_userid"]',
    'wpFields': '//input[@id="login_password"]',
    'logButton': '//button[@id="login_Login"]',
    'worldButton': '//li[@data-worldname="' + os.getenv("WORLD") + '"]',
    'previewButton': '//div[@class="toolbar_button premium"]',
    'farmTown': '//li[@class="farm_town_overview"]',
    'selectAll': '//a[@class="checkbox select_all"]',
    'claim': '//div[@id="fto_claim_button"]',
    'closeFirst': '//div[@style="height: auto; width: 800px; top: 141.5px; left: 50.5px; z-index: 1002;"]//button[@class="icon_right icon_type_speed ui-dialog-titlebar-close"]',
    'closeSecond': '//button[@class="icon_right icon_type_speed ui-dialog-titlebar-close"]',
    'message' : '//li[@class="messages main_menu_item first  "]',
    'islandView' : '//div[@class="option island_view circle_button js-option"]',
}

def setDriver():
	options = webdriver.ChromeOptions()
	# Pour "eviter" les anti-bots modification du user-agent"
	options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
	# Pour "eviter" les anti-bots et plus de confort mode "sans-tete" pas d'interface graphique du navigateur
	#options.add_argument("--headless")
	browser = webdriver.Chrome(options=options)
	return browser

class	Env:
	def __init__(self): 
		self.mdp = os.getenv("MDP")
		self.addrMail = os.getenv("MAIL")

# Pour click sur un bouton. xpath et frame -> expression type "//button[@title="Accepter et continuer"]". Si pas besoins de switch frame -> frame None
def switchFrameClickOn(browser, xpath, frame, minRand, maxRand):
	if frame != None:
		iframe = browser.find_element(By.XPATH, frame)
		browser.switch_to.frame(iframe)
	element = browser.find_element(By.XPATH, xpath)
	element.click()
	if frame != None:
		browser.switch_to.default_content()
	time.sleep(random.randint(minRand, maxRand))

# Pour remplir un champ. xpath -> expression type "//button[@title="Accepter et continuer"]". Key -> l'information a entrer dans le champs
def fillKey(browser, xpath, key):
	field = browser.find_element(By.XPATH, xpath)
	field.send_keys(key)

# Fait des actions "aleatoire". Toujours dans le but de diminuer les probabilites de detection par les anti-bots
def randAction(browser):
	switchFrameClickOn(browser, xpath_table['message'], None, 1, 3)
	switchFrameClickOn(browser, xpath_table['closeSecond'], None, 1, 3)
	switchFrameClickOn(browser, xpath_table['islandView'], None, 1, 3)

def connectGrepolis(browser, env):
	browser.get('https://fr.grepolis.com/')
	time.sleep(2)
	fillKey(browser, xpath_table['logFields'], env.addrMail)
	fillKey(browser,  xpath_table['wpFields'], env.mdp)
	switchFrameClickOn(browser,  xpath_table['logButton'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['worldButton'], None, 3, 5)

def farmVillage(browser):
	switchFrameClickOn(browser,  xpath_table['previewButton'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['farmTown'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['selectAll'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['claim'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['closeFirst'], None, 1, 3)
	switchFrameClickOn(browser,  xpath_table['closeSecond'], None, 1, 3)
	print("All the villages were collected")

def main():
	browser = setDriver()
	env = Env()
	connectGrepolis(browser, env)
	farmVillage(browser)
	randAction(browser)
	time.sleep(500)

if __name__ == "__main__":
	main()