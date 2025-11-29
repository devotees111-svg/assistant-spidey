import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        save_memory({"profile": {}, "facts": [], "history": []})
    return json.load(open(MEMORY_FILE))

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_memory(key, value):
    data = load_memory()
    data["profile"][key] = value
    save_memory(data)
    return f"Okay, I will remember your {key} is {value}."

def get_memory(key):
    data = load_memory()
    return data["profile"].get(key, "I don't remember that yet.")

def add_history(user_text):
    data = load_memory()
    data["history"].append(user_text)
    data["history"] = data["history"][-5:]  # keep only last 5
    save_memory(data)
