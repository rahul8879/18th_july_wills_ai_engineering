from config import settings
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=settings.pinecone_api_key)

pc.create_index(
    name=settings.pinecone_index_name,
    dimension=1536,
    metric="cosine",
    spec = ServerlessSpec(
        cloud="aws",
        region="us-east-1",
        
    )
)

print('index created')

