import json
from memory import load_memory, add_memory, get_memory, add_history
from tools import tool_weather, tool_search, tool_wiki, tool_open_app

# -----------------------
# LLM Placeholder (replace with Gemini/OpenAI)
# -----------------------
def call_llm(prompt: str):
    """
    Replace this function's body with a real LLM call.
    Example: Gemini, OpenAI, or Llama API.
    """
    print("LLM PROMPT:", prompt)
    return """
    {
        "tool": "none",
        "args": {},
        "response": "I am Spidey, running in mock mode — add real LLM API."
    }
    """

# -----------------------
# Agent Brain
# -----------------------
def agent_brain(user_text: str):
    memory = load_memory()
    add_history(user_text)

    prompt = f"""
    You are Assistant Spidey.
    User said: "{user_text}"

    Memory: {memory}

    Your task:
    - Detect user intent.
    - Choose correct tool.
    - Use memory when needed.

    Respond only in JSON in this format:
    {{
        "tool": "weather/search/wiki/open_app/memory_add/memory_get/none",
        "args": {{}},
        "response": "fallback message"
    }}
    """

    raw = call_llm(prompt)
    try:
        data = json.loads(raw)
    except:
        return "Error: LLM did not return valid JSON."

    return route_spidey(data)

# -----------------------
# Tool Router
# -----------------------
def route_spidey(data):
    tool = data["tool"]
    
    if tool == "weather":
        return tool_weather(**data["args"])
    if tool == "search":
        return tool_search(**data["args"])
    if tool == "wiki":
        return tool_wiki(**data["args"])
    if tool == "open_app":
        return tool_open_app(**data["args"])
    if tool == "memory_add":
        return add_memory(**data["args"])
    if tool == "memory_get":
        return get_memory(**data["args"])

    return data.get("response", "I couldn't process that.")
