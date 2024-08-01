import pytest
from decouple import config
from vector_search_engine.pinecone_utils import PineconeUtils

# Define test data
texts = ['hello', 'world']
embed_model = "text-embedding-ada-002"
index_name = 'test-index'
dimensions = 3
meta_data_config = {'indexed': ['channel_id', 'published']}

# Initialize PineconeUtils object with dummy API key and environment
pinecone_utils = PineconeUtils(api_key=config('PINECONE_API_KEY'), environment=config('PINECONE_ENV'))

def test_create_embeddings():
    # Test create_embeddings method
    embeddings = pinecone_utils.create_embeddings(texts, embed_model)
    assert isinstance(embeddings, list)
    assert len(embeddings) == len(texts)

def test_initialize_index():
    # Test initialize_index method
    index = pinecone_utils.initialize_index(index_name, dimensions, meta_data_config)
    assert isinstance(index, object)

def test_create_vector_object():
    # Test create_vector_object method
    id = 'test_id'
    values = [0.1, 0.2, 0.3]
    sparse_values = {'indices': [0, 1, 2], 'values': [0.1, 0.2, 0.3]}
    metadata = {'key': 'value'}
    vector_object = pinecone_utils.create_vector_object(id, values, sparse_values, metadata)
    assert isinstance(vector_object, dict)
    assert vector_object['id'] == id
    assert vector_object['values'] == values
    assert vector_object['sparseValues'] == sparse_values
    assert vector_object['metadata'] == metadata

def test_upsert_vectors():
    # Test upsert_vectors method
    vectors = [{'id': 'test_id1', 'values': [0.1, 0.2, 0.3]}, {'id': 'test_id2', 'values': [0.4, 0.5, 0.6]}]
    upsert_response = pinecone_utils.upsert_vectors(vectors, index_name)
    print(upsert_response,type(upsert_response))
    assert isinstance(upsert_response, object)

