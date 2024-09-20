import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.recall import calculate_recall


class TestCalculateRecall(unittest.TestCase):
    def test_basic_case(self):
        ground_truth_lists = [
            ["Paris is the capital of France", "The Eiffel Tower is in Paris"],
            ["William Shakespeare wrote Hamlet", "Hamlet is a tragedy"],
        ]
        float_lists = [[0.9, 0.8], [0.7, 0.6]]
        expected = [0.85, 0.65]
        result = calculate_recall(ground_truth_lists, float_lists)

        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=2)

    def test_empty_ground_truth(self):
        ground_truth_lists = [[], ["Some fact"]]
        float_lists = [[], [0.9]]
        expected = [0.0, 0.9]
        result = calculate_recall(ground_truth_lists, float_lists)

        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=2)

    def test_float_sum_exceeds_ground_truth(self):
        ground_truth_lists = [["Some fact", "Another fact"]]
        float_lists = [
            [1.0, 1.5]  # Сумма 2.5, но должно ограничиться 1.0
        ]
        expected = [1.0]
        result = calculate_recall(ground_truth_lists, float_lists)

        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=2)


unittest.main()
