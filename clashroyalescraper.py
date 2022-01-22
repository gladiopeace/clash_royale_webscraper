from bs4 import BeautifulSoup
import requests

html = requests.get('https://statsroyale.com/top/players').text
soup = BeautifulSoup(html, 'lxml')
# find all player name
names = soup.find_all('a', class_ = 'ui__blueLink topPlayers__name')

print ("Clash Royale Top Leaderboard")
print("")
# print each name, rank, and trophies in a loop
ranking = 1
i = 0
trophies = soup.find_all('div', class_ = 'topPlayers__cup')
for name in names:
    print("Rank", ranking, ":", name.text)
    print("Trophies:", trophies[i].text)
    print("")
    ranking += 1
    i += 1