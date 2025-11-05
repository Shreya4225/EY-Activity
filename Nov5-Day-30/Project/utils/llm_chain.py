from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os


def create_conversational_chain(retriever):
    """
    Create and return a ConversationalRetrievalChain configured with conversation memory.
    Automatically works with OpenRouter or OpenAI.
    """
    # 1️⃣ Create the LLM
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=float(os.getenv("OPENAI_TEMPERATURE", "0")),
        openai_api_base=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1"),
    )

    # 2️⃣ Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"  # ✅ explicitly define which output to store
    )

    # 3️⃣ Validate retriever
    if not hasattr(retriever, "get_relevant_documents"):
        raise ValueError("Retriever is invalid — make sure to use vectordb.as_retriever().")

    # 4️⃣ Create the chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer",  # ✅ critical fix for latest LangChain versions
    )

    return chain


