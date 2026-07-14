def precision_recall_at_k(recommended, relevant, k):
  """
  Compute precision@k and recall@k for a recommendation list.
  """
  # Write code here
  top_k = recommended[:k]
  relevant_set = set(relevant)

  hits = 0
  for i, value in enumerate(top_k):
    if value in relevant_set:
      hits += 1

  return [hits/k, hits/len(relevant)]