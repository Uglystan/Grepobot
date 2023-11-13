#include "Click.hpp"

void	init_localisation(std::map<std::string, t_point> &localisation)
{
	localisation = {
		{"activities", {50, 20}},
		{"rightScreen", {1900, 500}},
		{"middleScreen", {1250, 825}},
		{"apercu", {210, 120}},
		{"village", {210, 420}},
		{"recuperer", {1250, 825}},
		{"listTown", {950, 120}},
		{"firstTown", {950, 180}},
		{"test", {1825, 320}}
	};
}

int SwapToGame(Click const& grepobot, std::map<std::string, t_point> & localisation)
{
	int ret = 0;
	grepobot.doClick(localisation["activities"]);
	grepobot.doClick(localisation["rightScreen"]);
	grepobot.doClick(localisation["middleScreen"]);
	return (ret);
}

int AskVillage(Click const& grepobot, std::map<std::string, t_point> & localisation)
{
	int ret = 0;
	grepobot.doClick(localisation["apercu"]);
	grepobot.doClick(localisation["village"]);
	grepobot.doClick(localisation["recuperer"]);
	return (ret);
}

int SwapTown(Click const& grepobot, std::map<std::string, t_point> & localisation, int nbrTown)
{
	int ret = 0;
	grepobot.doClick(localisation["listTown"]);
	grepobot.doClick(localisation["firstTown"].destX, localisation["firstTown"].destY + nbrTown);
	return (ret);
}

int main(int argc, char **argv)
{
	if (argc == 2)
	{
		Click grepobot;
		std::map<std::string, t_point> localisation;
		int nbrTown = atoi(argv[1]);

		init_localisation(localisation);
		SwapToGame(grepobot, localisation);
		for(int i = 0; i < nbrTown; i++)
		{
			AskVillage(grepobot, localisation);
			SwapTown(grepobot, localisation, i * 20);
		}
		return 0;
	}
	std::cout << "Entrer le nombre de ville exemple : './AutoClick 7' pour 7 villes";
}
