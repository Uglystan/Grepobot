# My file
import main
import functionSel as selenium
from selenium.common.exceptions import NoSuchElementException
#Other file
import random
import time

# Connection au compte et selection du monde (serveur)
def connectGrepolis(browser, env):
	browser.get('https://fr.grepolis.com/')
	time.sleep(2)
	selenium.fillKey(browser, main.xpath_table['logFields'], env.addrMail)
	selenium.fillKey(browser, main.xpath_table['wpFields'], env.mdp)
	selenium.switchFrameClickOn(browser, main.xpath_table['logButton'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['worldButton'], None, 3, 5)
	try:
		selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 2)
	except NoSuchElementException:
		print("Nothing to close")

# Fait des actions "aleatoire". Toujours dans le but de diminuer les probabilites de detection par les anti-bots
def randAction(browser):
	selenium.switchFrameClickOn(browser, main.xpath_table['message'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['islandView'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['alliance'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['townView'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

# Recolte toutes les ressources de toutes les villes
def farmVillage(browser):
	selenium.switchFrameClickOn(browser, main.xpath_table['previewButton'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['farmTown'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['selectAll'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['claim'], None, 1, 3)
	# time.sleep(random.randint(600, 650))
	selenium.switchFrameClickOn(browser, main.xpath_table['closeVillage'], None, 1, 3)
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)
	print("All the villages were collected")

def farmThread(browser, mutex):
	while True:
		mutex.acquire()
		if random.randint(1, 2) == 1:
			randAction(browser)
		farmVillage(browser)
		if random.randint(1, 2) == 1:
			randAction(browser)
		mutex.release()
		time.sleep(random.randint(600, 650))