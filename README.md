# An intelligent Telegram bot engineered to fully automate customer support for a leading paints & coatings retail chain.
The bot delivers instant, accurate answers to customer inquiries about the company, career opportunities, products and services — powered by real-time data scraped directly from the website.
Link to the site of retail chain: https://centr-krasok.kz/?srsltid=AfmBOop5yL6zIbMUETuLVNaz8FBB7sE83TC4GBjazXBmG0dqCE2kHZYq

## Tech stack:
Python — core development language
LangChain — LLM pipeline orchestration
Groq API + Qwen3-32B — blazing-fast LLM inference
ChromaDB — vector database for semantic search
HuggingFace (intfloat/multilingual-e5-base) — multilingual embeddings (local model)
python-telegram-bot — Telegram integration
Guardrails — enforced via system prompt

## Architecture:
At its core lies a sophisticated two-stage RAG (Retrieval-Augmented Generation) pipeline: each incoming query is first intelligently reformulated by the LLM to maximize retrieval precision, followed by deep semantic search across the vector database — culminating in a context-aware response of the highest relevance. This architecture empowers the bot to handle everything from crystal-clear requests to the most ambiguous user inquiries with equal confidence and accuracy.
