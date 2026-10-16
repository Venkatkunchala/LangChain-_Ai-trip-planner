# LangChain Trip Planner — Prompt Templates Demo

This Streamlit app teaches LangChain Prompt Templates using a practical Trip Planner use case.

## Concepts Covered

1. Single-turn PromptTemplate
2. ChatPromptTemplate
3. Dynamic Variables
4. Multi-turn conversation using chat history

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Groq API Setup

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run:

```bash
streamlit run app.py
```

## Ollama Setup

Install Ollama, then run:

```bash
ollama pull qwen2.5:3b
streamlit run app.py
```

Then select **Ollama Local** in the sidebar.

## Important

`qwen2.5:3b` is an Ollama local model name.

For Groq, use models available in your Groq Console, such as:

```text
llama-3.3-70b-versatile
llama-3.1-8b-instant
```
