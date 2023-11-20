# My file
import farm
import cityData
import functionSel
# Other file
import threading
from dotenv import load_dotenv
import os
load_dotenv()

# Table de correspondance des boutton pour rendre le code plus durable si un chemin change on change ici et dans tout le code c'est bon
xpath_table = {
    'logFields' : '//input[@id="login_userid"]',
    'wpFields' : '//input[@id="login_password"]',
    'logButton' : '//button[@id="login_Login"]',
    'worldButton' : '//li[@data-worldname="' + os.getenv("WORLD") + '"]',
    'previewButton' : '//div[@class="toolbar_button premium"]',
    'farmTown' : '//li[@class="farm_town_overview"]',
    'selectAll' : '//a[@class="checkbox select_all"]',
    'claim' : '//div[@id="fto_claim_button"]',
    'closeVillage' : '//span[@class="ui-dialog-title" and contains(text(), "Villages de paysans")]/parent::div//button[@class="icon_right icon_type_speed ui-dialog-titlebar-close"]',
    'close' : '//button[@class="icon_right icon_type_speed ui-dialog-titlebar-close"]',
    'message' : '//li[@class="messages main_menu_item first  "]',
    'islandView' : '//div[@class="option island_view circle_button js-option"]',
    'alliance' : '//li[@class="allianceforum main_menu_item"]',
    'townView' : '//div[@class="option city_overview circle_button js-option"]',
    'senat' : '//div[@id="quickbar_dropdown0"]',
    'nextTownButton' : '//div[@class="btn_next_town button_arrow right"]',
    'villeName' : '//div[@class="town_name js-townname-caption js-rename-caption ui-game-selectable"]',
}

class	Env:
	def __init__(self): 
		self.mdp = os.getenv("MDP")
		self.addrMail = os.getenv("MAIL")

def main():
	browser = functionSel.setDriver()
	env = Env()
	mutex = threading.Lock()
	threadFarmVillage = threading.Thread(target=farm.farmThread, args=(browser,mutex,))
	threadBuild = threading.Thread(target=cityData.buildThread, args=(browser,mutex,))
	farm.connectGrepolis(browser, env)
	threadFarmVillage.start()
	threadBuild.start()

if __name__ == "__main__":
	main()