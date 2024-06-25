import faiss
import numpy as np

# Convert text to embeddings
text = "Hello, how are you?"
embeddings = get_embeddings(text).numpy().reshape(1, -1)

# Create index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(embeddings)

# Query the index
k = 1  # number of nearest neighbors
D, I = index.search(embeddings, k)
print("Distances:", D)
print("Indices:", I)
