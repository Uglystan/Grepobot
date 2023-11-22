# Grepobot
## Description
Welcome to Grepobot, a project I created to practice using Selenium while enhancing the gaming experience for [Grepolis](https://en.grepolis.com/) players. This bot has been developed to automate repetitive tasks such as resource collection and building construction, freeing up time for players to focus more on strategy.

Grepobot offers advanced customization features, allowing users to adjust settings according to their gaming preferences. Explore the potential of Grepobot and refer to the user guide for seamless integration of this solution into your Grepolis adventure.

**Important Note:** It is crucial to emphasize that the use of this bot may violate Grepolis' terms of service. It is strongly discouraged to use it for cheating or breaking the game rules. The bot's author takes no responsibility for any account sanctions resulting from its use. Use Grepobot responsibly.

## Getting Started

To get started with **Grepobot**, follow these steps:

1. **Make sure to have Python and Pip installed.**

2. **Clone the Repository:**

	In your terminal :
	```bash
   	git clone https://github.com/Uglystan/Grepobot ~/
	cd ~/Grepobot
3. **Create a `.env` File:**
	```bash
	touch .env
4. **Launch the script for install all requirement**
	```bash
	./script.sh

## Configuration with the `.env` File

To customize the bot's configuration, use the `.env` file. This file is intended to store sensitive or environment-specific parameters and is not tracked by Git for security reasons.

### Contents of the `.env` File

The `.env` file should contain the necessary information for the bot's automatic login and upgrading your city. This file should evolve as you found or colonize new cities. Make sure to add appropriate values for the following variables (If you want to see an example of the `.env` file, check the `env_example` file):

	
	AIL="test@gmail.com" (Your mail for login to Grepolis)
	MDP="password" (Your password for login to Grepolis)
	WORLD="BASILETOPIA" (World where you want to use the bot)
	NBRCITY="4" (Number of cities where you want to use the bot)
	CITY0"Sparta attTer" (Name of the city in the game with specialization "att" or "def" for attack or defense and "Ter" or "Nav" for land or naval)
	CITY1"Athens attNav"
	CITY2"Rome defTer"
	CITY3"Troy defNav"
	...

## Select your automation

By default, both the Farming bot and the Building bot are active, but you can choose to activate only one of them. To do this, simply go to the `main.py` file and comment out these lines to disable Building bot (Add "#" at the beginning): `threadBuild = threading.Thread(target=cityData.buildThread, args=(browser, mutex,))` and `threadBuild.start()`. To disable Farm bot comment : `threadFarmVillage = threading.Thread(target=farm.farmThread, args=(browser,mutex,))` and `threadFarmVillage.start()`.

## Run the bot

For run the bot just go in the file Grepobot and do:

	python main.py