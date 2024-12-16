import faiss
import numpy as np

def create_vector_store(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def retrieve_similar_chunks(query_embedding, index, k=5):
    distances, indices = index.search(np.array([query_embedding]), k)
    return indices[0]
