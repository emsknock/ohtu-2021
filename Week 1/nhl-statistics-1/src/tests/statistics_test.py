import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_initialiser(self):
        self.assertEqual(len(self.statistics._players), 5)

    def test_player_search_returns_correct_player(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_player_search_returns_none_when_doesnt_exist(self):
        self.assertEqual(self.statistics.search("Virtanen"), None)

    def test_players_by_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_top_scorers(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")