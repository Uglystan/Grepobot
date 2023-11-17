from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import random

def setDriver():
	options = webdriver.ChromeOptions()
	# Pour "eviter" les anti-bots modification du user-agent"
	options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
	# Pour "eviter" les anti-bots et plus de confort mode "sans-tete" pas d'interface graphique du navigateur
	#options.add_argument("--headless")
	browser = webdriver.Chrome(options=options)
	return browser

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

def switchFrameGetText(browser, xpath, frame) -> str:
	if frame != None:
		iframe = browser.find_element(By.XPATH, frame)
		browser.switch_to.frame(iframe)
	element = browser.find_element(By.XPATH, xpath).text
	if frame != None:
		browser.switch_to.default_content()
	return (element)