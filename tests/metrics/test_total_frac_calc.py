import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.substring_match import calculate_total_fraction_for_retrieved_chunks


class TestCalculateTotalFraction(unittest.TestCase):

    def test_full_matches(self):
        # Проверяем суммирование одинаковых retrieved_chunk в одном блоке
        data = [
            [
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.8},
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.7}
            ]
        ]
        expected = [[{"Paris is the capital of France": 1.5}]]
        result = calculate_total_fraction_for_retrieved_chunks(data)
        self.assertEqual(result, expected)

    def test_different_chunks(self):
        # Проверяем суммирование разных retrieved_chunk в одном блоке
        data = [
            [
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.8},
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is known for its landmarks", "fraction": 0.6}
            ]
        ]
        expected = [[
            {"Paris is the capital of France": 0.8},
            {"Paris is known for its landmarks": 0.6}
        ]]
        result = calculate_total_fraction_for_retrieved_chunks(data)
        self.assertEqual(result, expected)

    def test_multiple_blocks(self):
        # Проверяем работу с несколькими блоками данных
        data = [
            [
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.8},
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.7}
            ],
            [
                {"ground_truth": "Shakespeare wrote Hamlet", "retrieved_chunk": "William Shakespeare was a famous playwright", "fraction": 0.5},
                {"ground_truth": "Shakespeare wrote Hamlet", "retrieved_chunk": "Shakespeare was known for his plays", "fraction": 0.7}
            ]
        ]
        expected = [
            [{"Paris is the capital of France": 1.5}],
            [
                {"William Shakespeare was a famous playwright": 0.5},
                {"Shakespeare was known for his plays": 0.7}
            ]
        ]
        result = calculate_total_fraction_for_retrieved_chunks(data)
        self.assertEqual(result, expected)

    def test_empty_data(self):
        # Проверяем работу с пустыми данными
        data = []
        expected = []
        result = calculate_total_fraction_for_retrieved_chunks(data)
        self.assertEqual(result, expected)

    def test_unique_chunks(self):
        # Проверяем работу, если все retrieved_chunk уникальны и не дублируются
        data = [
            [
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France", "fraction": 0.8},
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is known for its landmarks", "fraction": 0.6}
            ]
        ]
        expected = [[
            {"Paris is the capital of France": 0.8},
            {"Paris is known for its landmarks": 0.6}
        ]]
        result = calculate_total_fraction_for_retrieved_chunks(data)
        self.assertEqual(result, expected)

    def test_incomplete_data(self):
        # Проверяем работу с некорректными данными (нет ключа 'fraction')
        data = [
            [
                {"ground_truth": "The Eiffel Tower is in Paris", "retrieved_chunk": "Paris is the capital of France"},
            ]
        ]
        with self.assertRaises(KeyError):
            calculate_total_fraction_for_retrieved_chunks(data)

unittest.main()
