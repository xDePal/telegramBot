from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

_ = load_dotenv()

llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)

# Rewrite the query
rewrite_prompt = ChatPromptTemplate.from_messages([
    ("system", "/no_think Ты помощник, который переформулирует вопрос пользователя в чёткий поисковый запрос для векторной базы данных. Верни только переформулированный запрос, без объяснений."),
    ("human", "{query}")
])

# Answer using context
answer_prompt = ChatPromptTemplate.from_messages([
    ("system", "/no_think Ты ассистент магазина и должен отвечать на вопросы клиентов, используя информацию из векторной базы данных. Если информация не найдена, скажи, что не можешь ответить на вопрос."),
    ("human", "Вопрос: {query}\n\nРезультаты поиска:\n{context}")
])

rewrite_chain = rewrite_prompt | llm
answer_chain = answer_prompt | llm