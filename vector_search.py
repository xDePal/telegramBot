from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base",
    model_kwargs={"device": "cuda"}
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

def search(query: str) -> str:
    results = vectorstore.similarity_search(query, k=5)
    
    context = ""
    for i, doc in enumerate(results, 1):
        context += f"--- Результат {i} ---\n{doc.page_content}\n\n"
    
    return context
