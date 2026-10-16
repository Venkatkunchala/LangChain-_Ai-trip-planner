from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model = "llama-3.1-8b-instant", temperature= 0)
response = model.invoke("Please explain about you in single sentence")
print(response.content)