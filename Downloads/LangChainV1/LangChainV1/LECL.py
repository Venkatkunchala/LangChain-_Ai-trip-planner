from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

summary_chain = (
    PromptTemplate.from_template(
        "Explain {topic} in one paragraph."
    )
    | llm
    | StrOutputParser()
)

chain = RunnableParallel(
    original_topic=RunnablePassthrough(),
    summary=summary_chain
)

result = chain.invoke({
    "topic": "LangChain"
})

print(result)