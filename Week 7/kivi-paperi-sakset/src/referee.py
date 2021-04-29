from moves import Move
from enum import IntEnum

class Result(IntEnum):
    P1 = 0
    P2 = 1
    DRAW = 2

class Referee:

    def __init__(self):
        self.points = [0, 0, 0] # P1, P2, DRAW, as in the enum

    def add_round(self, p1: Move, p2: Move):
        result = self._result(p1, p2)
        self.points[result] = self.points[result] + 1

    def _result(self, p1: Move, p2: Move):
        
        if p1 == p2:
            return Result.DRAW
        
        move_wins = {
            Move.ROCK: Move.SCISSORS,
            Move.PAPER: Move.ROCK,
            Move.SCISSORS: Move.PAPER,
        }

        return Result.P1 if move_wins[p1] == p2 else Result.P2

    def __str__(self):
        (p1, p2, draw) = self.points
        return (
            f"P1: {p1} — P2: {p2} — Tasapelit: {draw}"
        )