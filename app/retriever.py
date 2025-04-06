import requests

def hybrid_search(query, embedding_vector, opensearch_url):
    body = {
        "size": 5,
        "query": {
            "bool": {
                "must": [
                    {"match": {"text": query}},
                    {
                        "knn": {
                            "embedding": {
                                "vector": embedding_vector,
                                "k": 10
                            }
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(opensearch_url, json=body)
    return response.json()
