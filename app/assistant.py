import ollama
from app.memory import remember, get_memory


def run_assistant(user_input):

    command = user_input.lower()

    # Name memory
    if command.startswith("remember my name is"):
        name = user_input[len("remember my name is"):].strip()
        remember("name", name)
        return f"Okay, I will remember your name is {name}."

    # Preference memory
    if "i like" in command:
        preference = user_input.lower().replace("i like", "").strip()
        remember("preference", preference)
        return f"I'll remember that you like {preference}."

    # Fact memory
    if "my project is" in command:
        fact = user_input.lower().replace("my project is", "").strip()
        remember("fact", f"Project: {fact}")
        return f"I'll remember your project is {fact}."

    memory = get_memory()

    memory_context = ""

    if memory["name"]:
        memory_context += f"User name: {memory['name']}\n"

    if memory["facts"]:
        memory_context += "Facts: " + ", ".join(memory["facts"]) + "\n"

    if memory["preferences"]:
        memory_context += "Preferences: " + ", ".join(memory["preferences"]) + "\n"


    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": f"""
Your name is Vexa.
You are a personal AI assistant.

User memory:
{memory_context}

Use this memory when answering.
Be helpful and concise.
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]