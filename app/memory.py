import json
import os

MEMORY_FILE = "memory/user_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "name": "",
            "facts": [],
            "preferences": []
        }

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def remember(category, value):
    memory = load_memory()

    if category == "name":
        memory["name"] = value

    elif category == "fact":
        memory["facts"].append(value)

    elif category == "preference":
        memory["preferences"].append(value)

    save_memory(memory)


def get_memory():
    return load_memory()