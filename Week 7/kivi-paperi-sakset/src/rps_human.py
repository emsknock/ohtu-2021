from rps_player import RPS_Player
from moves import Move

class RPS_Human(RPS_Player):

    def move(self):
        move = input().lower()
        moves = {
            "k": Move.ROCK,
            "p": Move.PAPER,
            "s": Move.SCISSORS
        }
        return moves[move] if move in moves else Move.END

    def response(self, _):
        return self.move()