from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Query
query = "какие есть вакансии?"

def search(query):
    # Same embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-base",
        model_kwargs={"device": "cpu"}
    )

    # Load existing DB
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    results = vectorstore.similarity_search(
        query,
        k=3
    )

    for i, doc in enumerate(results, 1):
        return(f"Вопрос пользователя: {query}\n--- Результат {i} ---\n{doc.page_content}")
