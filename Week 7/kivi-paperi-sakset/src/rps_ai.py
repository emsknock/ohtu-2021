from rps_player import RPS_Player
from moves import Move, print_move

class RPS_Ai(RPS_Player):

    move_num = 0

    def response(self, prev: Move):
        self.move_num = (self.move_num + 1) % 3
        move = self.move_num
        print_move(move)
        return move