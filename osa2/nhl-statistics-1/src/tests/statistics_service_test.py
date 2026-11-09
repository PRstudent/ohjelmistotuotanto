import unittest
from statistics_service import StatisticsService
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
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
                PlayerReaderStub() #pylint: disable=line-too-long
            )

    def test_pelaaja_nimella(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.goals, 37)

    def test_ei_pelaajaa_vaaralla(self):
        player = self.stats.search("Selanne")
        self.assertAlmostEqual(player, None)

    def test_tiimin_pelaajat(self):
        players_det = self.stats.team("DET")

        player = players_det[0]

        self.assertAlmostEqual(player.name, "Yzerman")

    def test_top1(self):
        top = self.stats.top(1)
        self.assertAlmostEqual(top[0].name, "Gretzky")