import math


def calculate_dcg(fractions):
    """
    Вычисляет Discounted Cumulative Gain (DCG) для списка значений fraction.
    """
    dcg = 0.0
    for i, rel in enumerate(fractions):
        dcg += rel / math.log2(i + 2)  # Позиции начинаются с 1, поэтому i+2
    return dcg


def calculate_ndcg(retrieved_fractions):
    """
    Вычисляет NDCG для каждого списка retrieved_fractions.

    Args:
        retrieved_fractions (list): Список списков значений fraction для каждого retrieved_chunk.

    Returns:
        list: Список значений NDCG для каждого списка.
    """
    ndcg_values = []

    for fractions in retrieved_fractions:
        # Рассчитываем DCG
        dcg = calculate_dcg(fractions)

        # Рассчитываем идеальный DCG (IDCG), сортируя fractions по убыванию
        ideal_fractions = sorted(fractions, reverse=True)
        idcg = calculate_dcg(ideal_fractions)

        # Рассчитываем NDCG
        if idcg == 0:
            ndcg_values.append(0.0)
        else:
            ndcg_values.append(dcg / idcg)

    return ndcg_values

