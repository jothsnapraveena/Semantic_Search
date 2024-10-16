def search_vectors(index, query_vector, top_k=5):
    results = index.query(queries=[query_vector], top_k=top_k)
    return results
