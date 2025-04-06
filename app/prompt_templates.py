def build_prompt(context, user_query):
    return f"""
You are a helpful assistant. Use ONLY the context provided below to answer the question.

<context>
{context}
</context>

Question: {user_query}

Answer:
"""
