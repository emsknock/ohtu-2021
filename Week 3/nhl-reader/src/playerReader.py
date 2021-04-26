import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()
        self.players = list(
            map(lambda d : Player(d), response)
        )
        for player in self.players: print(player)