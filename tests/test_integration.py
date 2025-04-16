import unittest
import subprocess
import os
import glob

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestRankingToolIntegration(unittest.TestCase):

    def test_ranking(self):
        input_files = glob.glob(os.path.join(FIXTURE_DIR, 'input_*.txt'))

        for input_path in input_files:
            basename = os.path.basename(input_path).replace('input_', '').replace('.txt', '')
            expected_path = os.path.join(FIXTURE_DIR, f'expected_{basename}.txt')

            with self.subTest(case=basename):
                self.assertTrue(os.path.exists(expected_path), f"Missing expected file for {basename}")

                result = subprocess.run(
                    ['python', '-m', 'ranking_tool', 'rank', input_path],
                    capture_output=True,
                    text=True
                )

                with open(expected_path, 'r') as f:
                    expected = f.read().strip()

                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout.strip(), expected)
