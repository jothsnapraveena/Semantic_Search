import os
from dotenv import load_dotenv
from pinecone import ServerlessSpec

def load_config():
    load_dotenv()  # Load environment variables from .env

    # Load configuration values
    cloud = os.environ.get('PINECONE_CLOUD', 'aws')
    region = os.environ.get('PINECONE_REGION', 'us-east-1')
    environment = os.environ.get('PINECONE_ENVIRONMENT', 'us-west1-gcp')

    # Create the ServerlessSpec
    spec = ServerlessSpec(cloud=cloud, region=region)

    return environment, spec
