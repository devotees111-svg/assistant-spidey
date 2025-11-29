import wikipedia
import os
import requests

# ---------------- Weather Tool ----------------
def tool_weather(city):
    API_KEY = os.getenv("WEATHER_API_KEY")
    if not API_KEY:
        return "Weather API key not found."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        r = requests.get(url).json()
        temp = r["main"]["temp"]
        desc = r["weather"][0]["description"]
        return f"The weather in {city} is {temp}°C with {desc}."
    except:
        return "I could not get the weather right now."

# ---------------- Search Tool (simple) ----------------
def tool_search(query):
    return f"Search results for '{query}' (add SerpAPI or Gemini to enhance)."

# ---------------- Wikipedia Tool ----------------
def tool_wiki(topic):
    try:
        return wikipedia.summary(topic, sentences=2)
    except:
        return "No Wikipedia results found."

# ---------------- App Launcher Tool ----------------
def tool_open_app(app):
    apps = {
        "chrome": "start chrome",
        "notepad": "notepad",
        "cmd": "start cmd"
    }
    if app not in apps:
        return "I don't know that application."
    
    os.system(apps[app])
    return f"Opening {app}."
