from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=512, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", ","]
    )
    return splitter.split_text(text)
