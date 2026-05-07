from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "AI funnel automation",
    "Lead generation system",
    "Video content creation",
    "Voice AI assistant"
]

embeddings = model.encode(documents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))


def search_similar_text(query):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k=2)

    results = [documents[i] for i in indices[0]]

    return {
        "query": query,
        "similar_results": results
    }