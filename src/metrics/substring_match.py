import difflib
import re


def clean_text(text):
    """
    Очищает строку от лишних символов и приводит к нижнему регистру.
    """
    return re.sub(r"[^\w\s]", "", text).strip().lower()


def substring_match(g, r):
    """
    Определяет долю совпадения строки retrieved_chunk относительно ground_truth с использованием SequenceMatcher.
    """
    # Нормализуем строки
    g_clean = clean_text(g)
    r_clean = clean_text(r)

    # Разбиваем строки на слова
    g_words = g_clean.split()

    # Проверка: если ground_truth содержит меньше 3 слов, возвращаем 0
    if len(g_words) <= 3:
        raise ValueError("Кол-во слов в ground truth должно быть больше 3х.")

    if g_clean in r_clean:
        return 1.0  # Полное совпадение

    # Используем SequenceMatcher для поиска наибольшего совпадения
    matcher = difflib.SequenceMatcher(None, g_clean, r_clean)
    match = matcher.find_longest_match(0, len(g_clean), 0, len(r_clean))

    # Если не найдено совпадений или совпадение слишком короткое
    if match.size == 0:
        return 0

    # Извлекаем совпавший фрагмент
    matched_substring = g_clean[match.a : match.a + match.size]
    matched_words = matched_substring.split()

    # Проверка: если совпадение состоит из 3 слов или меньше, возвращаем 0
    if len(matched_words) <= 3:
        return 0

    r_starts_with_substring = r_clean.startswith(matched_substring)
    r_ends_with_substring = r_clean.endswith(matched_substring)

    if not r_starts_with_substring and not r_ends_with_substring:
        return 0
    elif r_starts_with_substring and not g_clean.endswith(matched_substring):
        return 0
    elif r_ends_with_substring and not g_clean.startswith(matched_substring):
        return 0

    # Вычисляем долю совпавших слов от общего количества слов в ground_truth
    return len(matched_words) / len(g_words)

def substring_match_for_lists(ground_truth, retrieved_chunks):
    """
    Рассчитывает substring_match для каждой строки из ground_truth по отношению к строкам из retrieved_chunks.
    Возвращает список списков словарей, где каждый словарь содержит 'ground_truth', 'retrieved_chunk' и 'fraction'.
    """
    results = []

    # Проходим по каждому вложенному списку строк
    for g_list, r_list in zip(ground_truth, retrieved_chunks):
        result_for_g_list = []

        for g in g_list:
            for r in r_list:
                fraction = substring_match(g, r)
                result_for_g_list.append(
                    {"ground_truth": g, "retrieved_chunk": r, "fraction": fraction}
                )

        results.append(result_for_g_list)

    return results


def calculate_total_fraction_for_retrieved_chunks(list_of_dicts):
    """
    Считает суммарные значения метрики fraction для каждого retrieved_chunk по каждому блоку данных,
    сохраняя структуру списка списков, где внутри находятся словари с retrieved_chunk и его суммой fractions.
    
    Args:
        list_of_dicts (list): Список списков со словарями, где каждый словарь содержит 'ground_truth',
                              'retrieved_chunk', 'fraction'.
    
    Returns:
        list: Список списков, где каждый внутренний список содержит словари с 'retrieved_chunk' и суммой 'fraction'.
    """
    result = []

    # Проходим по каждому блоку (внешний список)
    for inner_list in list_of_dicts:
        retrieved_chunk_sums = {}

        # Проходим по каждому словарю во вложенном списке
        for entry in inner_list:
            retrieved_chunk = entry['retrieved_chunk']
            fraction = entry['fraction']

            # Суммируем значения fraction для каждого retrieved_chunk
            if retrieved_chunk in retrieved_chunk_sums:
                retrieved_chunk_sums[retrieved_chunk] += fraction
            else:
                retrieved_chunk_sums[retrieved_chunk] = fraction

        # Преобразуем словарь с суммами в список словарей
        result_for_inner_list = [{chunk: sum_fraction} for chunk, sum_fraction in retrieved_chunk_sums.items()]
        
        # Добавляем в результат
        result.append(result_for_inner_list)

    return result

def get_fractions_by_retrieved_order(retrieved_chunks, list_of_dicts):
    """
    Возвращает значения fraction для каждого retrieved_chunk, сохраняя порядок следования retrieved_chunks.
    
    Args:
        retrieved_chunks (list): Список списков retrieved_chunks.
        list_of_dicts (list): Список списков словарей, где каждый словарь содержит ключ - 'retrieved_chunk',
                              и значение - сумму 'fraction'.
    
    Returns:
        list: Список списков значений fraction в порядке следования retrieved_chunks.
    """
    result = []

    # Проходим по каждому списку retrieved_chunks и соответствующему списку словарей
    for chunks_list, dict_list in zip(retrieved_chunks, list_of_dicts):
        fraction_values = []
        # Преобразуем список словарей в единый словарь для быстрого поиска по ключу
        dict_map = {list(d.keys())[0]: list(d.values())[0] for d in dict_list}
        
        # Проходим по каждому chunk и извлекаем его значение fraction
        for chunk in chunks_list:
            fraction_values.append(dict_map.get(chunk, 0))  # Если ключ не найден, возвращаем 0 по умолчанию
        
        result.append(fraction_values)

    return result