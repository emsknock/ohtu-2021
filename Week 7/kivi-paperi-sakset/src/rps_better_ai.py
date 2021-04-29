from collections import deque
from rps_player import RPS_Player
from moves import Move, print_move

class RPS_BetterAi(RPS_Player):

    def __init__(self, player_number: int, memory_size: int):
        super(self.__class__, self).__init__(player_number)
        self._memory = deque([], memory_size)

    def response(self, opponent_move: Move):
        
        # First two moves will always be rock
        if len(self._memory) < 3:
            self._memory.appendleft(opponent_move)
            print_move(Move.ROCK)
            return Move.ROCK

        # Gather stats of how the player has responded to this
        # move and respond accordingly

        my_last_move = self._memory[0]
        rps_stats = [0, 0, 0]

        # Indices from the first element to the penultimate element
        for i in range(0, len(self._memory) - 2):
            
            move = self._memory[i]
            prev = self._memory[i + 1]

            if prev == my_last_move:
                rps_stats[move] = rps_stats[move] + 1

        self._memory.appendleft(opponent_move)

        r, p, s = rps_stats
        move = Move.END
        if r > p or r > s:
            move = Move.PAPER
        elif p > r or p > s:
            move = Move.SCISSORS
        else:
            move = Move.ROCK
        
        print_move(move)
        return move

        