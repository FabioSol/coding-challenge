import unittest
from ranking_tool.utils import split_score_string


class TestUtils(unittest.TestCase):
    def test_split_score_string(self):
        self.assertEqual(split_score_string('team 1'), ('team', '1'))
        self.assertEqual(split_score_string('team 09'), ('team', '09'))
        self.assertEqual(split_score_string(' team 1 '), ('team', '1'))
        self.assertEqual(split_score_string(' team4 1 '), ('team4', '1'))
        self.assertEqual(split_score_string(' OG team 1 '), ('OG team', '1'))
        self.assertEqual(split_score_string('   OG. team 1 '), ('OG. team', '1'))
        self.assertEqual(split_score_string('   OG team 9 1000  '), ('OG team 9', '1000'))
        self.assertEqual(split_score_string(' \nteam 1 \n'), ('team', '1'))
        self.assertEqual(split_score_string(' \n\fteam 1 \n\f'), ('team', '1'))
