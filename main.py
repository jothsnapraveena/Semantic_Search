from semantic_search.config import load_config
from semantic_search.data_loader import load_data
from semantic_search.indexer import create_index, upsert_data
from semantic_search.search import search_vectors

def main():
    # Load configuration from .env
    load_config()

    # Load dataset
    data = load_data(r'D:\Semantic Search\data\arxiv-metadata-oai-snapshot.json')  # Update with your dataset path

    # Create Pinecone index
    index = create_index()

    # Upsert data into the index
    upsert_data(index, data)

    # Perform a search query
    query = "example search query"
    results = search_vectors(index, query)
    print(results)

if __name__ == "__main__":
    main()
