import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Init model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load as a list of dict
docs = []
with open("data/merged.jsonl", "r") as f:
    for line in f:
        docs.append(json.loads(line))

# Create document objects
documents = []

for d in docs:
    metadata = {}

    # add fields only if they exist
    for key in [
        "id", "source", "url", "name", "sku",
        "category", "subcategory",
        "price_current_kzt", "currency",
        "stock_almaty", "stock_astana"
    ]:
        if key in d and d[key] is not None:
            metadata[key] = d[key]

    doc = Document(
        page_content=d["text"],
        metadata=metadata
    )

    documents.append(doc)

# Create a vector db
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Query the vector db
results = vectorstore.similarity_search(
    "Чем занимается компания Центр Красок №1?",
    k=5
)

for r in results:
    print(r)