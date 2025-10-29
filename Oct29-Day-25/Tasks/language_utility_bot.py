# ============================================================
# Mini Language Utility Bot — Conversational Mistral Agent
# ============================================================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------

def count_words(sentence: str) -> str:
    """Count the number of words in a sentence."""
    word_count = len(sentence.split())
    return f"Agent: Your sentence has {word_count} words."


def reverse_text(sentence: str) -> str:
    """Reverse the word order in a sentence."""
    reversed_sentence = " ".join(sentence.split()[::-1])
    return f"Agent: {reversed_sentence}"


def define_word(word: str) -> str:
    """Define a word using the LLM."""
    prompt = f"Please provide a short definition or synonym for the word '{word}':"
    try:
        response = llm.invoke(prompt)
        return f"Agent: {response.content}"
    except Exception as e:
        return f"Agent: Could not define the word. Error: {e}"


def convert_case(text: str, case_type: str) -> str:
    """Convert text to uppercase or lowercase."""
    if case_type == "upper":
        return f"Agent: {text.upper()}"
    elif case_type == "lower":
        return f"Agent: {text.lower()}"
    else:
        return "Agent: Invalid case type. Use 'upper' or 'lower'."


def repeat_word(word: str, count: int) -> str:
    """Repeat a word a specified number of times."""
    return f"Agent: {' '.join([word] * count)}"


def print_history(memory: ConversationBufferMemory) -> str:
    """Print all previous inputs and outputs stored in memory."""
    history = memory.load_memory_variables({}).get("chat_history", [])
    if not history:
        return "Agent: No conversation history available."

    # Format the output nicely
    history_output = "Agent: Here is your conversation history:\n"
    for idx, message in enumerate(history):
        input_message = message['input']
        output_message = message['output']
        history_output += f"\nConversation {idx + 1}:\nYou: {input_message}\nAgent: {output_message}"

    return history_output


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Mini Language Utility Bot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Word Counter command
    if user_input.lower().startswith("count"):
        sentence = " ".join(user_input.split()[1:]).strip()
        if not sentence:
            print(
                "Agent: Please provide a sentence to count words. Example: count I am learning LangChain with Mistral.")
            continue
        print(count_words(sentence))
        memory.save_context({"input": user_input}, {"output": count_words(sentence)})
        continue

    # Handle Reverse Text command
    if user_input.lower().startswith("reverse"):
        sentence = " ".join(user_input.split()[1:]).strip()
        if not sentence:
            print("Agent: Please provide a sentence to reverse. Example: reverse LangChain is fun to learn.")
            continue
        print(reverse_text(sentence))
        memory.save_context({"input": user_input}, {"output": reverse_text(sentence)})
        continue

    # Handle Vocabulary Helper command
    if user_input.lower().startswith("define"):
        word = " ".join(user_input.split()[1:]).strip()
        if not word:
            print("Agent: Please provide a word to define. Example: define curious.")
            continue
        print(define_word(word))
        memory.save_context({"input": user_input}, {"output": define_word(word)})
        continue

    # Handle Uppercase / Lowercase command
    if user_input.lower().startswith("upper") or user_input.lower().startswith("lower"):
        case_type = user_input.split()[0].lower()
        text = " ".join(user_input.split()[1:]).strip()
        if not text:
            print("Agent: Please provide text to convert. Example: upper I like learning AI.")
            continue
        print(convert_case(text, case_type))
        memory.save_context({"input": user_input}, {"output": convert_case(text, case_type)})
        continue

    # Handle Word Repeater command
    if user_input.lower().startswith("repeat"):
        parts = user_input.split()
        if len(parts) != 3:
            print("Agent: Please use the format: repeat <word> <count>. Example: repeat hello 3.")
            continue
        word = parts[1]
        try:
            count = int(parts[2])
            print(repeat_word(word, count))
            memory.save_context({"input": user_input}, {"output": repeat_word(word, count)})
        except ValueError:
            print("Agent: Please provide a valid number for repetition.")
        continue

    # Handle History command
    if user_input.lower() == "history":
        print(print_history(memory))
        continue

    # Default: use LLM for other queries
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)

# # ============================================================
# # Mini Language Utility Bot — Conversational Mistral Agent
# # ============================================================
#
# import os
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
#
# # ------------------------------------------------------------
# # 1. Load environment variables
# # ------------------------------------------------------------
# load_dotenv()
# api_key = os.getenv("OPENROUTER_API_KEY")
# base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
#
# if not api_key:
#     raise ValueError("OPENROUTER_API_KEY not found in .env file")
#
# # ------------------------------------------------------------
# # 2. Initialize the Mistral model via OpenRouter
# # ------------------------------------------------------------
# llm = ChatOpenAI(
#     model="mistralai/mistral-7b-instruct",
#     temperature=0.4,
#     max_tokens=256,
#     api_key=api_key,
#     base_url=base_url,
# )
#
# # ------------------------------------------------------------
# # 3. Define helper tools
# # ------------------------------------------------------------
#
# def count_words(sentence: str) -> str:
#     """Count the number of words in a sentence."""
#     word_count = len(sentence.split())
#     return f"Agent: Your sentence has {word_count} words."
#
# def reverse_text(sentence: str) -> str:
#     """Reverse the word order in a sentence."""
#     reversed_sentence = " ".join(sentence.split()[::-1])
#     return f"Agent: {reversed_sentence}"
#
# def define_word(word: str) -> str:
#     """Define a word using the LLM."""
#     prompt = f"Please provide a short definition or synonym for the word '{word}':"
#     try:
#         response = llm.invoke(prompt)
#         return f"Agent: {response.content}"
#     except Exception as e:
#         return f"Agent: Could not define the word. Error: {e}"
#
# def convert_case(text: str, case_type: str) -> str:
#     """Convert text to uppercase or lowercase."""
#     if case_type == "upper":
#         return f"Agent: {text.upper()}"
#     elif case_type == "lower":
#         return f"Agent: {text.lower()}"
#     else:
#         return "Agent: Invalid case type. Use 'upper' or 'lower'."
#
# def repeat_word(word: str, count: int) -> str:
#     """Repeat a word a specified number of times."""
#     return f"Agent: {' '.join([word] * count)}"
#
# def print_history(memory: ConversationBufferMemory) -> str:
#     """Print all previous inputs and outputs stored in memory."""
#     history = memory.load_memory_variables({}).get("chat_history", [])
#     if not history:
#         return "Agent: No conversation history available."
#     return "Agent: Here is your conversation history:\n" + "\n".join(
#         [f"You: {entry['input']}\nAgent: {entry['output']}" for entry in history]
#     )
#
# # ------------------------------------------------------------
# # 4. Initialize memory
# # ------------------------------------------------------------
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
#
# # ------------------------------------------------------------
# # 5. Conversational loop
# # ------------------------------------------------------------
# print("\n=== Start chatting with your Mini Language Utility Bot ===")
# print("Type 'exit' to quit.\n")
#
# while True:
#     user_input = input("You: ").strip()
#     if user_input.lower() == "exit":
#         print("\nConversation ended.")
#         break
#
#     # Handle Word Counter command
#     if user_input.lower().startswith("count"):
#         sentence = " ".join(user_input.split()[1:]).strip()
#         if not sentence:
#             print("Agent: Please provide a sentence to count words. Example: count I am learning LangChain with Mistral.")
#             continue
#         print(count_words(sentence))
#         memory.save_context({"input": user_input}, {"output": count_words(sentence)})
#         continue
#
#     # Handle Reverse Text command
#     if user_input.lower().startswith("reverse"):
#         sentence = " ".join(user_input.split()[1:]).strip()
#         if not sentence:
#             print("Agent: Please provide a sentence to reverse. Example: reverse LangChain is fun to learn.")
#             continue
#         print(reverse_text(sentence))
#         memory.save_context({"input": user_input}, {"output": reverse_text(sentence)})
#         continue
#
#     # Handle Vocabulary Helper command
#     if user_input.lower().startswith("define"):
#         word = " ".join(user_input.split()[1:]).strip()
#         if not word:
#             print("Agent: Please provide a word to define. Example: define curious.")
#             continue
#         print(define_word(word))
#         memory.save_context({"input": user_input}, {"output": define_word(word)})
#         continue
#
#     # Handle Uppercase / Lowercase command
#     if user_input.lower().startswith("upper") or user_input.lower().startswith("lower"):
#         case_type = user_input.split()[0].lower()
#         text = " ".join(user_input.split()[1:]).strip()
#         if not text:
#             print("Agent: Please provide text to convert. Example: upper I like learning AI.")
#             continue
#         print(convert_case(text, case_type))
#         memory.save_context({"input": user_input}, {"output": convert_case(text, case_type)})
#         continue
#
#     # Handle Word Repeater command
#     if user_input.lower().startswith("repeat"):
#         parts = user_input.split()
#         if len(parts) != 3:
#             print("Agent: Please use the format: repeat <word> <count>. Example: repeat hello 3.")
#             continue
#         word = parts[1]
#         try:
#             count = int(parts[2])
#             print(repeat_word(word, count))
#             memory.save_context({"input": user_input}, {"output": repeat_word(word, count)})
#         except ValueError:
#             print("Agent: Please provide a valid number for repetition.")
#         continue
#
#     # Handle History command
#     if user_input.lower() == "history":
#         print(print_history(memory))
#         continue
#
#     # Default: use LLM for other queries
#     try:
#         response = llm.invoke(user_input)
#         print("Agent:", response.content)
#         memory.save_context({"input": user_input}, {"output": response.content})
#     except Exception as e:
#         print("Error:", e)
