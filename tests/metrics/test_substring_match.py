import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from metrics.substring_match import substring_match


class TestFractionInclusion(unittest.TestCase):
    # full match cases

    def test_full_match_identical(self):
        # Полное совпадение строк (идентичные строки)
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "Paris is the capital of France"
        expected_result = 1.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_full_match_with_extra_text_around(self):
        # Полное совпадение строк, где retrieved_chunk содержит в себе строку, но вокруг еще есть текст
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = (
            "The city of Paris is the capital of France and is known for its culture"
        )
        expected_result = 1.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_full_match_with_extra_text_after(self):
        # Полное совпадение строк, где retrieved_chunk содержит в себе строку и после идет какой-то текст
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "Paris is the capital of France and is beautiful"
        expected_result = 1.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_full_match_with_extra_text_before(self):
        # Полное совпадение строк, где retrieved_chunk содержит в себе строку, но перед ней есть текст
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "In Europe, Paris is the capital of France"
        expected_result = 1.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    # partial match cases

    def test_incorrect_partial_match_at_start(self):
        # Частичное совпадение с началом строки (совпадение больше 3 слов),
        # но неправильное. Потому что совпадение некорректное. См примеры
        ground_truth = "William Shakespeare wrote Hamlet"
        retrieved_chunk = "William Shakespeare wrote a great play"
        expected_result = 0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_correct_partial_match_at_start(self):
        # Частичное совпадение с началом строки (совпадение больше 3 слов)
        ground_truth = "William Shakespeare the writer wrote Hamlet"
        retrieved_chunk = "Shakespeare the writer wrote Hamlet, a great play"
        expected_result = 5 / 6
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_incorrect_partial_match_at_end(self):
        # Частичное совпадение с концом строки (совпадение больше 3 слов)
        # Некорректное. См. пример
        ground_truth = "The quick brown fox jumps over the lazy dog"
        retrieved_chunk = "Some ass bla bla bla over the lazy dog"
        expected_result = 0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_correct_partial_match_at_end(self):
        # Частичное совпадение с концом строки (совпадение больше 3 слов)
        # Корректное
        ground_truth = "The quick brown fox jumps over the lazy dog"
        retrieved_chunk = "word another and another then The quick brown fox jumps"
        expected_result = 5 / 9
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_proper_partial_match_at_start_less_than_3_words(self):
        # Частичное совпадение с началом строки (совпадение меньше 3 слов)
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "of France bla bla whatever"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_inproper_partial_match_at_start_less_than_3_words(self):
        # Частичное совпадение с началом строки (совпадение меньше 3 слов)
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "Paris is a beautiful city"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_proper_partial_match_at_end_less_than_3_words(self):
        # Частичное совпадение с концом строки (совпадение меньше 3 слов)
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "bla bla bla Paris is"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_improper_partial_match_at_end_less_than_3_words(self):
        # Частичное совпадение с концом строки (совпадение меньше 3 слов)
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "bla bla the capital"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_partial_match_in_middle_more_than_3_words(self):
        # Частичное совпадение в середине строки (больше 3 слов)
        ground_truth = "The quick brown fox jumps over the lazy dog"
        retrieved_chunk = "bla The fox jumps over the hill bla"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_partial_match_in_middle_less_than_3_words(self):
        # Частичное совпадение в середине строки (меньше 3 слов)
        ground_truth = "The quick brown fox jumps over the lazy dog"
        retrieved_chunk = "jumps over"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_no_match(self):
        # Нет совпадений
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "New York is a big city"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_ground_truth_less_than_3_words(self):
        # Ошибка: ground_truth содержит меньше 3 слов
        ground_truth = "Paris France"
        retrieved_chunk = "Paris France is beautiful"
        expected_result = 0.0
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)


class TestFractionInclusionAdditional(unittest.TestCase):
    def test_partial_match_overlap_start_and_end(self):
        # Частичное совпадение с началом и концом одновременно (overlap)
        ground_truth = "The quick brown fox jumps over the lazy dog"
        retrieved_chunk = "brown fox jumps over"
        expected_result = 0.0  # Совпадение в середине
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_full_match_in_middle(self):
        # Полное совпадение в середине строки
        ground_truth = "The capital of France is Paris"
        retrieved_chunk = (
            "Some text before The capital of France is Paris and more text after"
        )
        expected_result = 1.0  # Полное совпадение
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_partial_match_same_number_of_words_but_different_order(self):
        # Частичное совпадение с одинаковым количеством слов, но с разным порядком
        ground_truth = "The quick brown fox"
        retrieved_chunk = "fox quick brown The"
        expected_result = 0.0  # Порядок слов различен
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_partial_match_with_punctuation(self):
        # Частичное совпадение, но слова различаются только знаками препинания
        ground_truth = "The quick brown fox jumps over. the lazy dog."
        retrieved_chunk = "The quick .brown fox jumps over the lazy dog"
        expected_result = 1.0  # Игнорируем знаки препинания
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_empty_retrieved_chunk(self):
        # Пустая строка в retrieved_chunk
        ground_truth = "The quick brown fox"
        retrieved_chunk = ""
        expected_result = 0.0  # Пустая строка
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_both_empty_strings(self):
        # Полностью пустые строки должны вызывать ошибку ValueError
        ground_truth = ""
        retrieved_chunk = ""
        with self.assertRaises(ValueError):
            substring_match(ground_truth, retrieved_chunk)

    def test_case_insensitive_match(self):
        # Совпадение с разным регистром
        ground_truth = "Paris is the capital of France"
        retrieved_chunk = "paris is the capital of france"
        expected_result = 1.0  # Совпадение должно быть найдено, регистр игнорируется
        result = substring_match(ground_truth, retrieved_chunk)
        self.assertAlmostEqual(result, expected_result, places=2)


unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(TestFractionInclusion)
)
# Запуск дополнительных тестов
unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(TestFractionInclusionAdditional)
)
