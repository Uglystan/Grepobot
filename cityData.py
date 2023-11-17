#My file
import functionSel as selenium
import main
# Other file
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os

# Table de correspondance pour les niveaux des batiements et pour cliquer sur les boutons upgrade
xpath_senat = {
	'senat' : '//div[@id="building_main_main"]//a[@class="button_build build_up build small"]',
	'scierie' : '//div[@id="building_main_lumber"]//a[@class="button_build build_up build small"]',
	'ferme' : '//div[@id="building_main_farm"]//a[@class="button_build build_up build small"]',
	'carriere' : '//div[@id="building_main_stoner"]//a[@class="button_build build_up build small"]',
	'entrepot' : '//div[@id="building_main_storage"]//a[@class="button_build build_up build small"]',
	'mineArgent' : '//div[@id="building_main_ironer"]//a[@class="button_build build_up build small"]',
	'caserne' : '//div[@id="building_main_barracks"]//a[@class="button_build build_up build small"]',
	'temple' : '//div[@id="building_main_temple"]//a[@class="button_build build_up build small"]',
	'marche' : '//div[@id="building_main_market"]//a[@class="button_build build_up build small"]',
	'port' : '//div[@id="building_main_docks"]//a[@class="button_build build_up build small"]',
	'academie' : '//div[@id="building_main_academy"]//a[@class="button_build build_up build small"]',
	'rempart' : '//div[@id="building_main_wall"]//a[@class="button_build build_up build small"]',
	'grotte' : '//div[@id="building_main_hide"]//a[@class="button_build build_up build small"]',
	'lvlSenat' : '//div[@id="building_main_main"]//span[@class="level white"]',
	'lvlScierie' : '//div[@id="building_main_lumber"]//span[@class="level white"]',
	'lvlFerme' : '//div[@id="building_main_farm"]//span[@class="level white"]',
	'lvlCarriere' : '//div[@id="building_main_stoner"]//span[@class="level white"]',
	'lvlEntrepot' : '//div[@id="building_main_storage"]//span[@class="level white"]',
	'lvlMineArgent' : '//div[@id="building_main_ironer"]//span[@class="level white"]',
	'lvlCaserne' : '//div[@id="building_main_barracks"]//span[@class="level white"]',
	'lvlTemple' : '//div[@id="building_main_temple"]//span[@class="level white"]',
	'lvlMarche' : '//div[@id="building_main_market"]//span[@class="level white"]',
	'lvlPort' : '//div[@id="building_main_docks"]//span[@class="level white"]',
	'lvlAcademie' : '//div[@id="building_main_academy"]//span[@class="level white"]',
	'lvlRempart' : '//div[@id="building_main_wall"]//span[@class="level white"]',
	'lvlGrotte' : '//div[@id="building_main_hide"]//span[@class="level white"]',
}

# Class avec toutes les informations utiles d'une ville
class City:
	def __init__(self, browser, nameCity, typeCity):
		self.name = nameCity
		self.type = typeCity
		self.lvlSenat = int(selenium.switchFrameGetText(browser, xpath_senat['lvlSenat'], None))
		self.lvlScierie = int(selenium.switchFrameGetText(browser, xpath_senat['lvlScierie'], None))
		self.lvlFerme = int(selenium.switchFrameGetText(browser, xpath_senat['lvlFerme'], None))
		self.lvlCarriere = int(selenium.switchFrameGetText(browser, xpath_senat['lvlCarriere'], None))
		self.lvlEntrepot = int(selenium.switchFrameGetText(browser, xpath_senat['lvlEntrepot'], None))
		self.lvlMineArgent = int(selenium.switchFrameGetText(browser, xpath_senat['lvlMineArgent'], None))
		self.lvlCaserne = int(selenium.switchFrameGetText(browser, xpath_senat['lvlCaserne'], None))
		self.lvlTemple = int(selenium.switchFrameGetText(browser, xpath_senat['lvlTemple'], None))
		self.lvlMarche = int(selenium.switchFrameGetText(browser, xpath_senat['lvlMarche'], None))
		self.lvlPort = int(selenium.switchFrameGetText(browser, xpath_senat['lvlPort'], None))
		self.lvlAcademie = int(selenium.switchFrameGetText(browser, xpath_senat['lvlAcademie'], None))
		self.lvlRempart = int(selenium.switchFrameGetText(browser, xpath_senat['lvlRempart'], None))
		self.lvlGrotte = int(selenium.switchFrameGetText(browser, xpath_senat['lvlGrotte'], None))

# Met dans un Vecteur une class City initilise pour chaque ville renseigne dans le .env
def getInfoCity(browser, vecteurCity):
	i = 0
	while i < int(os.getenv("NBRCITY")):
		nameCity = os.getenv("CITY" + str(i)).split()[0]
		typeCity = os.getenv("CITY" + str(i)).split()[1]
		if nameCity == selenium.switchFrameGetText(browser, main.xpath_table['villeName'], None):#nom ville
			selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
			vecteurCity.append(City(browser, nameCity, typeCity))
			selenium.switchFrameClickOn(browser, main.xpath_table['closeSecond'], None, 1, 2)
			i+=1
		else:
			#throw erreur si i > int(os.getenv("NBRCITY"))
			selenium.switchFrameClickOn(browser, main.xpath_table['nextTownButton'], None, 1, 3)#next

def buildThread(browser):
	vecteurCity = []
	getInfoCity(browser, vecteurCity)
	for city in vecteurCity:
		if prerequis = 1
		else if partie 1 = 1
		else if partie 2 = 1
		else
	# selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	# print("test" + browser.find_element(By.XPATH, xpath_senat['lvlSenat']).text)
	# try :
	# 	browser.find_element(By.XPATH, xpath_senat['senat'])
	# except NoSuchElementException :
	# 	print("Pas possible")

# Pre requis Directe apres fondation si tout ca est bon on passe a la suite sinon on fait ca
# Caserne lvl 5
# Temple lvl 3
# Marche lvl 4
# Senat lvl 14

# Une fois les pre requis valide Partie 1
# Scierie : 20
# Carrière : 20
# Mine d'argent : 20
# Sénat : 16
# Ferme : 15
# Enrepôt : 15
# Caserne : 12
# Temple : 8
# Marché : 10
# Port : 8
# Académie : 8
# Remparts : 10
# Grotte : 3

# Partie 2
# Scierie : 25
# Carrière : 25
# Mine d'argent : 25
# Sénat : 17
# Ferme : 20
# Entrepôt : 20 (22 si céramique non recherché à l'académie).
# Caserne : 13
# Temple : 9
# Marché : 10
# Port : 20
# Académie : 28 (avec bateau de colonisation recherché, et conquête recherché).
# Remparts : 12
# Grotte : 5

#Spe attaque terrestre
# Scierie : 25
# Carrière : 40
# Mine d'argent : 40
# Sénat : 24
# Ferme : 40
# Entrepôt : 30 (22 si céramique non recherché à l'académie).
# Caserne : 30
# Temple : 25
# Marché : 20
# Port : 20
# Académie : 30 (avec bateau de colonisation recherché, et conquête recherché).
# Remparts : 25
# Grotte : 10

#Spe attaque naval
# Scierie : 40
# Carrière : 40
# Mine d'argent : 40
# Sénat : 24
# Ferme : 40
# Entrepôt : 30 (22 si céramique non recherché à l'académie).
# Caserne : 10
# Temple : 25
# Marché : 20
# Port : 30
# Académie : 30 (avec bateau de colonisation recherché, et conquête recherché).
# Remparts : 25
# Grotte : 10

#Spe defense terreste
# Scierie : 25
# Carrière : 40
# Mine d'argent : 40
# Sénat : 24
# Ferme : 40
# Entrepôt : 30 (22 si céramique non recherché à l'académie).
# Caserne : 30
# Temple : 25
# Marché : 20
# Port : 20
# Académie : 30 (avec bateau de colonisation recherché, et conquête recherché).
# Remparts : 25
# Grotte : 10

#Spe defense naval
# Scierie : 40
# Carrière : 40
# Mine d'argent : 40
# Sénat : 24
# Ferme : 40
# Entrepôt : 30 (22 si céramique non recherché à l'académie).
# Caserne : 10
# Temple : 25
# Marché : 20
# Port : 30
# Académie : 30 (avec bateau de colonisation recherché, et conquête recherché).
# Remparts : 25
# Grotte : 10