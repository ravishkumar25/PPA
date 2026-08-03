import json
import ollama
from app.memory import get_memory, save_memory


def analyze_memory(user_input):

    prompt = f"""
You are an AI memory analyzer.

Analyze the user's message.

Remember ONLY long-term information.

Return ONLY JSON.

Examples:

{{"remember": false}}

{{"remember": true, "category":"preference", "value":"Likes horror games"}}

User:
{user_input}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:
        return json.loads(response["message"]["content"])
    except:
        return {"remember": False}


def save_ai_memory(memory_result):

    if not memory_result.get("remember"):
        return

    memory = get_memory()

    category = memory_result["category"]
    value = memory_result["value"]

    if category == "name":
        memory["name"] = value

    elif category == "fact":
        memory["facts"].append(value)

    elif category == "preference":
        memory["preferences"].append(value)

    save_memory(memory)