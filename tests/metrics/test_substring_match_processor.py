import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.substring_match import substring_match_for_lists


class TestCalculateInclusionForLists(unittest.TestCase):
    def test_calculate_inclusion_basic(self):
        ground_truth = [
            ["Paris is the capital of France", "William Shakespeare wrote Hamlet"],
            ["The quick brown fox jumps over the lazy dog"],
        ]

        retrieved_chunks = [
            ["The capital of France is Paris", "Shakespeare was a famous playwright"],
            ["The fox jumps over", "The quick brown dog sleeps"],
        ]

        result = substring_match_for_lists(ground_truth, retrieved_chunks)
        # Проверка, что структура результата сохранена
        self.assertEqual(len(result), 2)  # Два списка
        self.assertEqual(
            len(result[0]), 4
        )  # Первый список содержит 4 результата (2 ground_truth * 2 retrieved_chunks)
        self.assertEqual(
            len(result[1]), 2
        )  # Второй список содержит 2 результата (1 ground_truth * 2 retrieved_chunks)

        # Проверка значения для первой строки
        self.assertEqual(result[0][0]["ground_truth"], "Paris is the capital of France")
        self.assertEqual(
            result[0][0]["retrieved_chunk"], "The capital of France is Paris"
        )
        self.assertAlmostEqual(result[0][0]["fraction"], 4 / 6, places=2)

        # Проверка значения для второй строки
        self.assertEqual(result[0][1]["ground_truth"], "Paris is the capital of France")
        self.assertEqual(
            result[0][1]["retrieved_chunk"], "Shakespeare was a famous playwright"
        )
        self.assertAlmostEqual(result[0][1]["fraction"], 0.0, places=2)

        # Проверка значения для третьей строки (William Shakespeare wrote Hamlet)
        self.assertEqual(
            result[0][2]["ground_truth"], "William Shakespeare wrote Hamlet"
        )
        self.assertEqual(
            result[0][2]["retrieved_chunk"], "The capital of France is Paris"
        )
        self.assertAlmostEqual(result[0][2]["fraction"], 0.0, places=2)

    def test_calculate_inclusion_empty_retrieved(self):
        # Тест, если retrieved_chunks пуст
        ground_truth = [["Some string"]]
        retrieved_chunks = [[]]

        result = substring_match_for_lists(ground_truth, retrieved_chunks)
        self.assertEqual(
            len(result[0]), 0
        )  # Для пустого retrieved_chunks нет сопоставлений


unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(TestCalculateInclusionForLists)
)
