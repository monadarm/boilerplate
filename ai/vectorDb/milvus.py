from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
import numpy as np

# Connect to Milvus server
connections.connect("default", host="localhost", port="19530")

# Define schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768)
]
schema = CollectionSchema(fields, "text embedding")

# Create collection
collection = Collection("text_embeddings", schema)

# Convert text to embeddings
text = "Hello, how are you?"
embeddings = get_embeddings(text).numpy().tolist()

# Insert data
collection.insert([embeddings])

# Create index
index_params = {"index_type": "IVF_FLAT", "params": {"nlist": 100}, "metric_type": "COSINE"}
collection.create_index("embedding", index_params)

# Load collection
collection.load()

# Search
search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
results = collection.search([embeddings], "embedding", search_params, limit=1)
for result in results:
    print(result)
