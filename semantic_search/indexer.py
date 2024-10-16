import pinecone
from semantic_search.config import load_config

def create_index():
    environment, spec = load_config()

    # Initialize Pinecone
    pinecone.init(api_key=os.environ['PINECONE_API_KEY'], environment=environment)

    # Create the index if it doesn't exist
    index_name = 'semantic-search-index'
    existing_indexes = pinecone.list_indexes()

    if index_name not in existing_indexes:
        pinecone.create_index(index_name, dimension=384, metric='dotproduct', spec=spec)

    return pinecone.Index(index_name)

def upsert_data(index, data):
    for batch in data:  # Assuming 'data' is a list of dicts with 'id' and 'embedding' keys
        index.upsert(vectors=[(item['id'], item['embedding']) for item in batch])
