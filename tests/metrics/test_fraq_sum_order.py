import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.substring_match import get_fractions_by_retrieved_order


class TestGetFractionsByRetrievedOrder(unittest.TestCase):
    def test_full_match(self):
        # Тест на полное совпадение
        retrieved_chunks = [
            ["Paris is the capital of France", "Paris is known for its landmarks"]
        ]
        list_of_dicts = [
            [
                {"Paris is the capital of France": 1.5},
                {"Paris is known for its landmarks": 1.5},
            ]
        ]
        expected = [[1.5, 1.5]]
        result = get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts)
        self.assertEqual(result, expected)

    def test_missing_value(self):
        # Тест на отсутствие некоторых значений
        retrieved_chunks = [
            [
                "Paris is the capital of France",
                "Paris is known for its landmarks",
                "Unknown chunk",
            ]
        ]
        list_of_dicts = [
            [
                {"Paris is the capital of France": 1.5},
                {"Paris is known for its landmarks": 1.5},
            ]
        ]
        expected = [[1.5, 1.5, 0]]  # Для "Unknown chunk" должно быть 0
        result = get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts)
        self.assertEqual(result, expected)

    def test_empty_lists(self):
        # Тест на работу с пустыми списками
        retrieved_chunks = []
        list_of_dicts = []
        expected = []
        result = get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts)
        self.assertEqual(result, expected)

    def test_order_preserved(self):
        # Тест на правильное соответствие порядка
        retrieved_chunks = [
            ["Paris is known for its landmarks", "Paris is the capital of France"]
        ]
        list_of_dicts = [
            [
                {"Paris is the capital of France": 1.5},
                {"Paris is known for its landmarks": 1.0},
            ]
        ]
        expected = [[1.0, 1.5]]  # Должен быть соблюден порядок chunks
        result = get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts)
        self.assertEqual(result, expected)

    def test_multiple_blocks(self):
        # Тест с несколькими блоками данных
        retrieved_chunks = [
            ["Paris is the capital of France", "Paris is known for its landmarks"],
            [
                "William Shakespeare was a famous playwright",
                "Shakespeare was known for his plays",
            ],
        ]
        list_of_dicts = [
            [
                {"Paris is the capital of France": 1.5},
                {"Paris is known for its landmarks": 1.5},
            ],
            [
                {"William Shakespeare was a famous playwright": 0.9},
                {"Shakespeare was known for his plays": 1.3},
            ],
        ]
        expected = [[1.5, 1.5], [0.9, 1.3]]
        result = get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts)
        self.assertEqual(result, expected)


unittest.main()
