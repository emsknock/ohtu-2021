from enum import IntEnum

class Move(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    END = 3

def print_move(move: Move):
    names = {
        Move.ROCK: "K",
        Move.PAPER: "P",
        Move.SCISSORS: "S",
        Move.END: "-"
    }
    print(names[move])