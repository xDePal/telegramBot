import re
import threading
from tg_bot import run_bot
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from vector_search import search

load_dotenv()

llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Ты ассистент магазина и должен отвечать на вопросы клиентов, используя информацию из векторной базы данных. Если информация не найдена, скажи, что не можешь ответить на вопрос. Не размышляй, а отвечай"),
    ("human", "Вопрос: {query}\n\nРезультаты поиска:\n{context}")
])

chain = prompt | llm

def ask(query: str) -> str:
    context = search(query)
    response = chain.invoke({"query": query, "context": context})
    return re.sub(r"<think>.*?</think>", "", response.content, flags=re.DOTALL).strip()

def main():
    # Run bot in background thread so it doesn't block
    #bot_thread = threading.Thread(target=run_bot, daemon=True)
    #bot_thread.start()

    # Test query directly
    answer = ask("чем занимается компания?")
    print(answer)

    # Keep main thread alive for the bot
    #bot_thread.join()

if __name__ == "__main__":
    main()

