

# import pandas as pd
# from collections import Counter
# import math

# def substring_match(g, r):
#     """
#     Calculate the fraction of words in the ground truth chunk 'g' that are present in the retrieved chunk 'r'.
#     """
#     g_words = g.split()
#     r_words = r.split()
#     g_counter = Counter(g_words)
#     r_counter = Counter(r_words)
#     overlap_counter = g_counter & r_counter
#     overlapping_word_count = sum(overlap_counter.values())
#     total_word_count = sum(g_counter.values())
#     fraction = overlapping_word_count / total_word_count if total_word_count > 0 else 0
#     return fraction

# def compute_metrics(ground_truth_chunks, retrieved_chunks):
#     """
#     Compute the recall-like metric and NDCG for a single query.
#     """
#     # Metric 1: Recall-like metric
#     max_fractions_per_g = []
#     for g in ground_truth_chunks:
#         max_fraction = 0
#         for r in retrieved_chunks:
#             fraction = substring_match(g, r)
#             if fraction > max_fraction:
#                 max_fraction = fraction
#         max_fractions_per_g.append(max_fraction)
#     recall_metric = sum(max_fractions_per_g) / len(ground_truth_chunks) if len(ground_truth_chunks) > 0 else 0

#     # Metric 2: NDCG
#     relevance_scores = []
#     for r in retrieved_chunks:
#         max_fraction = 0
#         for g in ground_truth_chunks:
#             fraction = substring_match(g, r)
#             if fraction > max_fraction:
#                 max_fraction = fraction
#         relevance_scores.append(max_fraction)
#     # Compute DCG
#     dcg = 0
#     for i, rel in enumerate(relevance_scores):
#         position = i + 1
#         dcg += rel / math.log2(position + 1)
#     # Compute IDCG
#     sorted_relevance_scores = sorted(relevance_scores, reverse=True)
#     idcg = 0
#     for i, rel in enumerate(sorted_relevance_scores):
#         position = i + 1
#         idcg += rel / math.log2(position + 1)
#     ndcg = dcg / idcg if idcg > 0 else 0
#     return recall_metric, ndcg

# # Example usage with a pandas DataFrame
# # Assume df is your DataFrame with 'query', 'ground_truth_chunks', and 'retrieved_chunks' columns

# # df = pd.read_csv('your_dataset.csv')  # Load your dataset

# # For demonstration, here's a sample DataFrame
# data = {
#     'query': ['What is the capital of France?', 'Who wrote Hamlet?'],
#     'ground_truth_chunks': [['Paris is the capital city of France.'], ['William Shakespeare wrote Hamlet.']],
#     'retrieved_chunks': [['Paris is known for the Eiffel Tower.', 'France has many tourist attractions.'],
#                          ['Hamlet is a play by Shakespeare.', 'It is one of his most famous works.']]
# }

# df = pd.DataFrame(data)

# # Compute metrics for each query
# recall_metrics = []
# ndcg_metrics = []

# for index, row in df.iterrows():
#     ground_truth_chunks = row['ground_truth_chunks']
#     retrieved_chunks = row['retrieved_chunks']
#     recall_metric, ndcg_metric = compute_metrics(ground_truth_chunks, retrieved_chunks)
#     recall_metrics.append(recall_metric)
#     ndcg_metrics.append(ndcg_metric)

# # Add the metrics to the DataFrame
# df['Recall_Metric'] = recall_metrics
# df['NDCG_Metric'] = ndcg_metrics

# print(df[['query', 'Recall_Metric', 'NDCG_Metric']])

# # Calculate average metrics over all queries
# average_recall = sum(recall_metrics) / len(recall_metrics) if len(recall_metrics) > 0 else 0
# average_ndcg = sum(ndcg_metrics) / len(ndcg_metrics) if len(ndcg_metrics) > 0 else 0

# print(f'Average Recall Metric: {average_recall}')
# print(f'Average NDCG Metric: {average_ndcg}')
