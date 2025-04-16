import unittest
from ranking_tool.core import Game, League


class TestGame(unittest.TestCase):
    def test_calculate_points(self):
        tie = (1, 1)
        self.assertEqual(Game.calculate_points(0, 0), tie)
        self.assertEqual(Game.calculate_points(50000, 50000), tie)
        self.assertEqual(Game.calculate_points(1, 1), tie)
        self.assertEqual(Game.calculate_points(-1, -1), tie)

        win_first = (3, 0)
        self.assertEqual(Game.calculate_points(1, 0), win_first)
        self.assertEqual(Game.calculate_points(-5, -100), win_first)
        self.assertEqual(Game.calculate_points(10001, 10000), win_first)
        self.assertEqual(Game.calculate_points(10, -1), win_first)

        win_second = (0, 3)
        self.assertEqual(Game.calculate_points(0, 1), win_second)
        self.assertEqual(Game.calculate_points(-5, 4), win_second)
        self.assertEqual(Game.calculate_points(-5, -4), win_second)
        self.assertEqual(Game.calculate_points(100, 101), win_second)

    def test_from_string(self):
        self.assertEqual(Game.from_string('dogs 4, bulls 8').points, {'dogs': 0, 'bulls': 3})
        self.assertEqual(Game.from_string('Dogs 4, Bulls 8').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('Dogs 4 , Bulls 8').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('Dogs 4 , Bulls 8 ').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('   Dogs 4 , Bulls 8 ').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('\nDogs 4 , Bulls 8 ').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('Dogs 4 , Bulls 8 \n').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('Dogs 4 , Bulls 8 \n\f').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('     Dogs 04      ,   Bulls 8     ').points, {'Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('FC Dogs 4 , Bulls 8 ').points, {'FC Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string(' FC  . Dogs 4 , Bulls 8 ').points, {'FC  . Dogs': 0, 'Bulls': 3})
        self.assertEqual(Game.from_string('Dogs4567 4 , Bulls6 8 \n\f').points, {'Dogs4567': 0, 'Bulls6': 3})

        with self.assertRaises(ValueError):
            Game.from_string('')
        with self.assertRaises(ValueError):
            Game.from_string(', , ,')
        with self.assertRaises(ValueError):
            Game.from_string('fghj')
        with self.assertRaises(ValueError):
            Game.from_string('Dogs , Bulls')
        with self.assertRaises(ValueError):
            Game.from_string('Dogs 4 , Bulls')
        with self.assertRaises(ValueError):
            Game.from_string('Dogs , Bulls 5')
        with self.assertRaises(ValueError):
            Game.from_string('Dogs6, Bulls5')
        with self.assertRaises(ValueError):
            Game.from_string('Dogs 6 Bulls 5')


class TestLeague(unittest.TestCase):
    def test_calculate_ranking(self):
        game_list = [Game.from_string('Lions 3, Snakes 3'),
                     Game.from_string('Tarantulas 1, FC Awesome 0'),
                     Game.from_string('Lions 1, FC Awesome 1'),
                     Game.from_string('Tarantulas 3, Snakes 1'),
                     Game.from_string('Lions 4, Grouches 0')]

        self.assertEqual(League.calculate_ranking(game_list),
                         [(1, 'Tarantulas', 6), (2, 'Lions', 5), (3, "FC Awesome", 1), (3, "Snakes", 1),
                          (5, 'Grouches', 0)])

    def test_from_string(self):
        s = 'Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\nLions 1, FC Awesome 1\nTarantulas 3, Snakes 1\nLions 4, Grouches 0'
        self.assertEqual(League.from_string(s).games, [Game.from_string('Lions 3, Snakes 3'),
                                                       Game.from_string('Tarantulas 1, FC Awesome 0'),
                                                       Game.from_string('Lions 1, FC Awesome 1'),
                                                       Game.from_string('Tarantulas 3, Snakes 1'),
                                                       Game.from_string('Lions 4, Grouches 0')])

    def test_to_string(self):
        s = 'Lions 3, Snakes 3\nTarantulas 1, FC Awesome 0\nLions 1, FC Awesome 1\nTarantulas 3, Snakes 1\nLions 4, Grouches 0'
        res = '1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pt\n3. Snakes, 1 pt\n5. Grouches, 0 pts'
        self.assertEqual(League.from_string(s).__str__(), res)
