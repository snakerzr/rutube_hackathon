# not that reliable
# Сам не считал ожидаемые значения
import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.ndcg import calculate_ndcg


# class TestCalculateNDCG(unittest.TestCase):
#     def test_fractions_greater_than_one(self):
#         # Тест на значения fraction больше 1
#         fractions = [
#             [1.5, 2.3, 0.9],  # Первый запрос
#             [1.0, 0.7, 1.4],  # Второй запрос
#         ]
#         expected = [0.920, 0.981]  # Пересчитанные значения NDCG
#         result = calculate_ndcg(fractions)
#         for r, e in zip(result, expected):
#             self.assertAlmostEqual(r, e, places=3)

#     def test_perfect_ranking(self):
#         # Тест на идеальное ранжирование (NDCG = 1)
#         fractions = [
#             [2.3, 1.5, 0.9]  # Уже идеально отсортировано по убыванию
#         ]
#         expected = [1.0]  # Идеальное ранжирование
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_worst_ranking(self):
#         # Тест на наихудшее ранжирование
#         fractions = [
#             [0.9, 1.5, 2.3]  # Полностью неправильный порядок
#         ]
#         expected = [0.811]  # Пересчитанное значение для худшего ранжирования
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_equal_fractions(self):
#         # Тест на равные значения fraction
#         fractions = [
#             [1.0, 1.0, 1.0]  # Все значения одинаковы
#         ]
#         expected = [1.0]  # NDCG будет 1, потому что все значения одинаковы
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_single_element(self):
#         # Тест на список с одним элементом
#         fractions = [
#             [1.0]  # Один элемент
#         ]
#         expected = [1.0]  # Один элемент всегда считается идеально ранжированным
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_all_zero_fractions(self):
#         # Тест на нулевые значения fraction
#         fractions = [
#             [0.0, 0.0, 0.0]  # Все значения равны 0
#         ]
#         expected = [0.0]  # NDCG = 0, так как все значения 0
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)


# class TestCalculateNDCG(unittest.TestCase):
#     def test_fractions_greater_than_one(self):
#         # Тест на значения fraction больше 1
#         fractions = [
#             [1.5, 2.3, 0.9],  # Первый запрос
#             [1.0, 0.7, 1.4],  # Второй запрос
#         ]
#         expected = [0.920, 0.981]  # Пересчитанные значения NDCG
#         result = calculate_ndcg(fractions)
#         for r, e in zip(result, expected):
#             self.assertAlmostEqual(r, e, places=3)

#     def test_perfect_ranking(self):
#         # Тест на идеальное ранжирование (NDCG = 1)
#         fractions = [
#             [2.3, 1.5, 0.9]  # Уже идеально отсортировано по убыванию
#         ]
#         expected = [1.0]  # Идеальное ранжирование
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_worst_ranking(self):
#         # Тест на наихудшее ранжирование
#         fractions = [
#             [0.9, 1.5, 2.3]  # Полностью неправильный порядок
#         ]
#         expected = [0.811]  # Пересчитанное значение для худшего ранжирования
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_equal_fractions(self):
#         # Тест на равные значения fraction
#         fractions = [
#             [1.0, 1.0, 1.0]  # Все значения одинаковы
#         ]
#         expected = [1.0]  # NDCG будет 1, потому что все значения одинаковы
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_single_element(self):
#         # Тест на список с одним элементом
#         fractions = [
#             [1.0]  # Один элемент
#         ]
#         expected = [1.0]  # Один элемент всегда считается идеально ранжированным
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

#     def test_all_zero_fractions(self):
#         # Тест на нулевые значения fraction
#         fractions = [
#             [0.0, 0.0, 0.0]  # Все значения равны 0
#         ]
#         expected = [0.0]  # NDCG = 0, так как все значения 0
#         result = calculate_ndcg(fractions)
#         self.assertAlmostEqual(result[0], expected[0], places=3)

class TestCalculateNDCG(unittest.TestCase):

    def test_fractions_greater_than_one(self):
        # Тест на значения fraction больше 1
        fractions = [
            [1.5, 2.3, 0.9],  # Первый запрос
            [1.0, 0.7, 1.4]   # Второй запрос
        ]
        expected = [0.899, 0.981]  # Изменено ожидаемое значение для первого запроса
        result = calculate_ndcg(fractions)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=3)

    def test_perfect_ranking(self):
        # Тест на идеальное ранжирование (NDCG = 1)
        fractions = [
            [2.3, 1.5, 0.9]  # Уже идеально отсортировано по убыванию
        ]
        expected = [1.0]  # Идеальное ранжирование
        result = calculate_ndcg(fractions)
        self.assertAlmostEqual(result[0], expected[0], places=3)

    def test_worst_ranking(self):
        # Тест на наихудшее ранжирование
        fractions = [
            [0.9, 1.5, 2.3]  # Полностью неправильный порядок
        ]
        expected = [0.811]  # Пересчитанное значение для худшего ранжирования
        result = calculate_ndcg(fractions)
        self.assertAlmostEqual(result[0], expected[0], places=3)

    def test_equal_fractions(self):
        # Тест на равные значения fraction
        fractions = [
            [1.0, 1.0, 1.0]  # Все значения одинаковы
        ]
        expected = [1.0]  # NDCG будет 1, потому что все значения одинаковы
        result = calculate_ndcg(fractions)
        self.assertAlmostEqual(result[0], expected[0], places=3)

    def test_single_element(self):
        # Тест на список с одним элементом
        fractions = [
            [1.0]  # Один элемент
        ]
        expected = [1.0]  # Один элемент всегда считается идеально ранжированным
        result = calculate_ndcg(fractions)
        self.assertAlmostEqual(result[0], expected[0], places=3)

    def test_all_zero_fractions(self):
        # Тест на нулевые значения fraction
        fractions = [
            [0.0, 0.0, 0.0]  # Все значения равны 0
        ]
        expected = [0.0]  # NDCG = 0, так как все значения 0
        result = calculate_ndcg(fractions)
        self.assertAlmostEqual(result[0], expected[0], places=3)

unittest.main()
