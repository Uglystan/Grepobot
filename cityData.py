#My file
import functionSel as selenium
import main
# Other file
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import random
import time

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
			selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 2)
			i+=1
		else:
			#throw erreur si i > int(os.getenv("NBRCITY"))
			selenium.switchFrameClickOn(browser, main.xpath_table['nextTownButton'], None, 1, 3)#next

def checkBuildPrerequisite(city) -> int:
	if city.lvlCaserne >= 5 and city.lvlTemple >= 8 and city.lvlMarche >= 10 and city.lvlSenat >= 14:
		return (1)
	else:
		return (0)

def checkBuildPart1(city) -> int:
	if city.lvlCaserne >= 12 and city.lvlTemple >= 3 and city.lvlMarche >= 4 and city.lvlSenat >= 16 and city.lvlScierie >= 20 and city.lvlCarriere >= 20 and city.lvlMineArgent >= 20 and city.lvlFerme >= 15 and city.lvlEntrepot >= 15 and city.lvlPort >= 8 and city.lvlAcademie >= 8 and city.lvlRempart >= 10 and city.lvlGrotte >= 3:
		return (1)
	else:
		return (0)

def checkBuildPart2(city) -> int:
	if city.lvlCaserne >= 13 and city.lvlTemple >= 9 and city.lvlMarche >= 10 and city.lvlSenat >= 17 and city.lvlScierie >= 25 and city.lvlCarriere >= 25 and city.lvlMineArgent >= 25 and city.lvlFerme >= 20 and city.lvlEntrepot >= 20 and city.lvlPort >= 20 and city.lvlAcademie >= 28 and city.lvlRempart >= 12 and city.lvlGrotte >= 5:
		return (1)
	else:
		return (0)

def checkBuildTer(city) -> int:
	if city.type == "attTer" or city.type == "defTer":
		if city.lvlCaserne >= 30 and city.lvlTemple >= 25 and city.lvlMarche >= 20 and city.lvlSenat >= 24 and city.lvlScierie >= 25 and city.lvlCarriere >= 40 and city.lvlMineArgent >= 40 and city.lvlFerme >= 40 and city.lvlEntrepot >= 30 and city.lvlPort >= 20 and city.lvlAcademie >= 30 and city.lvlRempart >= 25 and city.lvlGrotte >= 10:
			return (1)
		else:
			return (0)
	return (1)

def checkBuildNav(city) -> int:
	if city.type == "attNav" or city.type == "defNav":
		if city.lvlCaserne >= 10 and city.lvlTemple >= 25 and city.lvlMarche >= 20 and city.lvlSenat >= 24 and city.lvlScierie >= 40 and city.lvlCarriere >= 40 and city.lvlMineArgent >= 40 and city.lvlFerme >= 40 and city.lvlEntrepot >= 30 and city.lvlPort >= 30 and city.lvlAcademie >= 30 and city.lvlRempart >= 25 and city.lvlGrotte >= 10:
			return (1)
		else:
			return (0)
	return (1)

def buildPrerequisite(browser, city):
	selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	i = 0
	while i < 4:
		try:
			if city.lvlSenat < 14 and i == 0:
				selenium.switchFrameClickOn(browser, xpath_senat['senat'], None, 1, 2)
				i+=1
			if city.lvlTemple < 3 and i == 1:
				selenium.switchFrameClickOn(browser, xpath_senat['temple'], None, 1, 2)
				i+=1
			if city.lvlCaserne < 5 and i == 2:
				selenium.switchFrameClickOn(browser, xpath_senat['caserne'], None, 1, 2)
				i+=1
			if city.lvlMarche < 4 and i == 3:
				selenium.switchFrameClickOn(browser, xpath_senat['marche'], None, 1, 2)
				i+=1
			i+=1
		except NoSuchElementException:
			i+=1
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

def buildPart1(browser, city):
	selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	i = 0
	while i < 13:
		try:
			if city.lvlScierie < 20 and i == 0:
				selenium.switchFrameClickOn(browser, xpath_senat['scierie'], None, 1, 2)
				i+=1
			if city.lvlCarriere < 20 and i == 1:
				selenium.switchFrameClickOn(browser, xpath_senat['carriere'], None, 1, 2)
				i+=1
			if city.lvlMineArgent < 20 and i == 2:
				selenium.switchFrameClickOn(browser, xpath_senat['mineArgent'], None, 1, 2)
				i+=1
			if city.lvlFerme < 15 and i == 3:
				selenium.switchFrameClickOn(browser, xpath_senat['ferme'], None, 1, 2)
				i+=1
			if city.lvlEntrepot < 15 and i == 4:
				selenium.switchFrameClickOn(browser, xpath_senat['entrepot'], None, 1, 2)
				i+=1
			if city.lvlSenat < 16 and i == 5:
				selenium.switchFrameClickOn(browser, xpath_senat['senat'], None, 1, 2)
				i+=1
			if city.lvlTemple < 8 and i == 6:
				selenium.switchFrameClickOn(browser, xpath_senat['temple'], None, 1, 2)
				i+=1
			if city.lvlRempart < 10 and i == 7:
				selenium.switchFrameClickOn(browser, xpath_senat['rempart'], None, 1, 2)
				i+=1
			if city.lvlAcademie < 8 and i == 8:
				selenium.switchFrameClickOn(browser, xpath_senat['academie'], None, 1, 2)
				i+=1
			if city.lvlCaserne < 12 and i == 9:
				selenium.switchFrameClickOn(browser, xpath_senat['caserne'], None, 1, 2)
				i+=1
			if city.lvlPort < 8 and i == 10:
				selenium.switchFrameClickOn(browser, xpath_senat['port'], None, 1, 2)
				i+=1
			if city.lvlMarche < 10 and i == 11:
				selenium.switchFrameClickOn(browser, xpath_senat['marche'], None, 1, 2)
				i+=1
			if city.lvlGrotte < 3 and i == 12:
				selenium.switchFrameClickOn(browser, xpath_senat['grotte'], None, 1, 2)
				i+=1
			i+=1
		except NoSuchElementException:
			i+=1
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

def buildPart2(browser, city):
	selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	i = 0
	while i < 12:
		try:
			if city.lvlScierie < 25 and i == 0:
				selenium.switchFrameClickOn(browser, xpath_senat['scierie'], None, 1, 2)
				i+=1
			if city.lvlCarriere < 25 and i == 1:
				selenium.switchFrameClickOn(browser, xpath_senat['carriere'], None, 1, 2)
				i+=1
			if city.lvlMineArgent < 25 and i == 2:
				selenium.switchFrameClickOn(browser, xpath_senat['mineArgent'], None, 1, 2)
				i+=1
			if city.lvlFerme < 20 and i == 3:
				selenium.switchFrameClickOn(browser, xpath_senat['ferme'], None, 1, 2)
				i+=1
			if city.lvlEntrepot < 20 and i == 4:
				selenium.switchFrameClickOn(browser, xpath_senat['entrepot'], None, 1, 2)
				i+=1
			if city.lvlSenat < 17 and i == 5:
				selenium.switchFrameClickOn(browser, xpath_senat['senat'], None, 1, 2)
				i+=1
			if city.lvlTemple < 9 and i == 6:
				selenium.switchFrameClickOn(browser, xpath_senat['temple'], None, 1, 2)
				i+=1
			if city.lvlRempart < 12 and i == 7:
				selenium.switchFrameClickOn(browser, xpath_senat['rempart'], None, 1, 2)
				i+=1
			if city.lvlAcademie < 28 and i == 8:
				selenium.switchFrameClickOn(browser, xpath_senat['academie'], None, 1, 2)
				i+=1
			if city.lvlCaserne < 13 and i == 9:
				selenium.switchFrameClickOn(browser, xpath_senat['caserne'], None, 1, 2)
				i+=1
			if city.lvlPort < 20 and i == 10:
				selenium.switchFrameClickOn(browser, xpath_senat['port'], None, 1, 2)
				i+=1
			if city.lvlGrotte < 5 and i == 11:
				selenium.switchFrameClickOn(browser, xpath_senat['grotte'], None, 1, 2)
				i+=1
			i+=1
		except NoSuchElementException:
			i+=1
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

def buildTer(browser, city):
	selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	i = 0
	while i < 12:
		try:
			if city.lvlScierie < 25 and i == 0:
				selenium.switchFrameClickOn(browser, xpath_senat['scierie'], None, 1, 2)
				i+=1
			if city.lvlCarriere < 40 and i == 1:
				selenium.switchFrameClickOn(browser, xpath_senat['carriere'], None, 1, 2)
				i+=1
			if city.lvlMineArgent < 40 and i == 2:
				selenium.switchFrameClickOn(browser, xpath_senat['mineArgent'], None, 1, 2)
				i+=1
			if city.lvlFerme < 40 and i == 3:
				selenium.switchFrameClickOn(browser, xpath_senat['ferme'], None, 1, 2)
				i+=1
			if city.lvlEntrepot < 30 and i == 4:
				selenium.switchFrameClickOn(browser, xpath_senat['entrepot'], None, 1, 2)
				i+=1
			if city.lvlSenat < 24 and i == 5:
				selenium.switchFrameClickOn(browser, xpath_senat['senat'], None, 1, 2)
				i+=1
			if city.lvlTemple < 25 and i == 6:
				selenium.switchFrameClickOn(browser, xpath_senat['temple'], None, 1, 2)
				i+=1
			if city.lvlRempart < 25 and i == 7:
				selenium.switchFrameClickOn(browser, xpath_senat['rempart'], None, 1, 2)
				i+=1
			if city.lvlAcademie < 30 and i == 8:
				selenium.switchFrameClickOn(browser, xpath_senat['academie'], None, 1, 2)
				i+=1
			if city.lvlCaserne <30 and i == 9:
				selenium.switchFrameClickOn(browser, xpath_senat['caserne'], None, 1, 2)
				i+=1
			if city.lvlMarche < 20 and i == 10:
				selenium.switchFrameClickOn(browser, xpath_senat['marche'], None, 1, 2)
				i+=1
			if city.lvlGrotte < 10 and i == 11:
				selenium.switchFrameClickOn(browser, xpath_senat['grotte'], None, 1, 2)
				i+=1
			i+=1
		except NoSuchElementException:
			i+=1
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

def buildNav(browser, city):
	selenium.switchFrameClickOn(browser, main.xpath_table['senat'], None, 1, 3)
	i = 0
	while i < 12:
		try:
			if city.lvlScierie < 40 and i == 0:
				selenium.switchFrameClickOn(browser, xpath_senat['scierie'], None, 1, 2)
				i+=1
			if city.lvlCarriere < 40 and i == 1:
				selenium.switchFrameClickOn(browser, xpath_senat['carriere'], None, 1, 2)
				i+=1
			if city.lvlMineArgent < 40 and i == 2:
				selenium.switchFrameClickOn(browser, xpath_senat['mineArgent'], None, 1, 2)
				i+=1
			if city.lvlFerme < 40 and i == 3:
				selenium.switchFrameClickOn(browser, xpath_senat['ferme'], None, 1, 2)
				i+=1
			if city.lvlEntrepot < 30 and i == 4:
				selenium.switchFrameClickOn(browser, xpath_senat['entrepot'], None, 1, 2)
				i+=1
			if city.lvlSenat < 24 and i == 5:
				selenium.switchFrameClickOn(browser, xpath_senat['senat'], None, 1, 2)
				i+=1
			if city.lvlTemple < 25 and i == 6:
				selenium.switchFrameClickOn(browser, xpath_senat['temple'], None, 1, 2)
				i+=1
			if city.lvlRempart < 25 and i == 7:
				selenium.switchFrameClickOn(browser, xpath_senat['rempart'], None, 1, 2)
				i+=1
			if city.lvlAcademie < 30 and i == 8:
				selenium.switchFrameClickOn(browser, xpath_senat['academie'], None, 1, 2)
				i+=1
			if city.lvlPort < 30 and i == 9:
				selenium.switchFrameClickOn(browser, xpath_senat['port'], None, 1, 2)
				i+=1
			if city.lvlMarche < 20 and i == 10:
				selenium.switchFrameClickOn(browser, xpath_senat['marche'], None, 1, 2)
				i+=1
			if city.lvlGrotte < 10 and i == 11:
				selenium.switchFrameClickOn(browser, xpath_senat['grotte'], None, 1, 2)
				i+=1
			i+=1
		except NoSuchElementException:
			i+=1
	selenium.switchFrameClickOn(browser, main.xpath_table['close'], None, 1, 3)

def goToCity(browser, city):
	while selenium.switchFrameGetText(browser, main.xpath_table['villeName'], None) != city.name:
		selenium.switchFrameClickOn(browser, main.xpath_table['nextTownButton'], None, 2, 3)

def buildThread(browser, mutex):
	vecteurCity = []
	while True:
		mutex.acquire()
		getInfoCity(browser, vecteurCity)
		for city in vecteurCity:
			goToCity(browser, city)
			if checkBuildPrerequisite(city) == 0:
				buildPrerequisite(browser, city)
			elif checkBuildPart1(city) == 0:
				buildPart1(browser, city)
			elif checkBuildPart2(city) == 0:
				buildPart2(browser, city)
			elif checkBuildTer(city) == 0:
				buildTer(browser, city)
			elif checkBuildNav(city) == 0:
				buildNav(browser, city)
		mutex.release()
		time.sleep(random.randint(900, 1000))
		vecteurCity.clear()

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