from chunker import chunk_text
from embedder import get_bedrock_embedding
from retriever import hybrid_search
from prompt_templates import build_prompt
from bedrock_client import query_bedrock_claude

def run_rag_pipeline(document_text, user_query, opensearch_url):
    chunks = chunk_text(document_text)
    embedded_chunks = [(chunk, get_bedrock_embedding(chunk)) for chunk in chunks]
    query_embedding = get_bedrock_embedding(user_query)
    retrieved = hybrid_search(user_query, query_embedding, opensearch_url)

    context = "\n".join([hit["_source"]["text"] for hit in retrieved["hits"]["hits"]])
    prompt = build_prompt(context, user_query)
    return query_bedrock_claude(prompt)
