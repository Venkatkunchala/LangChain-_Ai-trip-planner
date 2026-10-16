from langchain_ollama import ChatOllama


model = ChatOllama(model = "qwen2.5:3b")
response = model.invoke("Who are you? explain in a sentence!")
print(response.content)