def calculate_recall(ground_truth_lists, float_lists):
    """
    Рассчитывает значение recall для каждого списка ground_truth.
    
    Args:
        ground_truth_lists (list): Список списков со строками ground_truth.
        float_lists (list): Список списков с флоатами, которые соответствуют значению метрик для каждого ground_truth.
    
    Returns:
        list: Список значений recall (float от 0 до 1) для каждого блока данных.
    """
    recall_values = []

    # Проходим по каждому списку ground_truth и соответствующему списку с float
    for ground_truth, float_list in zip(ground_truth_lists, float_lists):
        num_ground_truth = len(ground_truth)  # Количество строк в ground_truth

        if num_ground_truth == 0:
            recall_values.append(0.0)  # Если ground_truth пуст, recall = 0
        else:
            total_floats = sum(float_list)  # Суммируем все значения float
            recall = total_floats / num_ground_truth  # Делим сумму флоатов на количество строк ground_truth
            recall_values.append(min(recall, 1.0))  # Убеждаемся, что recall не превышает 1

    return recall_values

ground_truth_lists = [
    ["Paris is the capital of France", "The Eiffel Tower is in Paris"],
    ["William Shakespeare wrote Hamlet", "Hamlet is a tragedy", "Shakespeare was known for his plays"]
]

float_lists = [
    [0.9, 0.8],  # Для первого блока
    [0.7, 0.6, 0.5]  # Для второго блока
]

result = calculate_recall(ground_truth_lists, float_lists)

print(result)
