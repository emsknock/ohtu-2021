from referee import Referee
from moves import Move

from rps_player import RPS_Player
from rps_human import RPS_Human
from rps_ai import RPS_Ai
from rps_better_ai import RPS_BetterAi

class RPS:
    
    def __init__(self, p1: RPS_Player, p2: RPS_Player):
        self.p1 = p1
        self.p2 = p2

    def play(self):

        referee = Referee()

        while True:
            
            print("Pelaajan 1 siirto > ")
            p1_move = self.p1.move()

            if p1_move == Move.END:
                print("Peli loppui. Kiitos!")
                print(referee)
                break

            print("Pelaajan 2 siirto > ")
            p2_move = self.p2.response(p1_move)
            
            referee.add_round(p1_move, p2_move)

    @staticmethod
    def player_vs_player():
        return RPS(RPS_Human(1), RPS_Human(2))

    @staticmethod
    def player_vs_simple_ai():
        return RPS(RPS_Human(1), RPS_Ai(2))

    @staticmethod
    def player_vs_better_ai():
        return RPS(RPS_Human(1), RPS_BetterAi(2, 10)) 