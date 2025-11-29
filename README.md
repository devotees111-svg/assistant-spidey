# assistant-spidey
Voice‑driven AI assistant with Gemini‑ADK style tools, MCP‑based memory system, and modular agent architecture. Built as a capstone project for the Kaggle Agents Intensive course.

# 🕷️ Assistant Spidey – Voice‑Driven AI Agent (Gemini‑ADK Inspired, MCP Memory)

Assistant Spidey is a **voice‑controlled AI agent** built for the  
**Kaggle Agents Intensive Capstone Project**.

It combines:

- 🎤 **Speech Recognition**  
- 🤖 **LLM Agent Brain (Gemini/OpenAI style reasoning)**  
- 🧰 **Tool System (like Gemini ADK)**  
- 💾 **Memory Engine (MCP‑style long‑term memory)**  
- 🗣 **Text‑to‑Speech responses**  
- 🖥 **Desktop app control**  
- 🌐 **Live data tools (weather, web search, Wikipedia)**  
- 🔊 **Kaggle‑friendly simulation using WAV audio files**

This repo contains the full source code, demo files, and documentation for running and modifying Assistant Spidey.

---

## 🚀 Features

### ✅ Voice Commands  
Spidey listens to your voice and executes commands such as:

- “What’s the weather in Mumbai?”  
- “Who is Iron Man?”  
- “Open Chrome.”  
- “Remember that my name is Abhishek.”  
- “What is my name?”  
- “Search for Avengers release date.”

### ✅ Gemini ADK‑Inspired Tool System  
Modular **tools** (Python functions) that the agent can call:

- 🌤 Weather Tool  
- 🌐 Web Search Tool  
- 📚 Wikipedia Tool  
- 🖥 App Launcher Tool  
- 📝 Memory Add Tool  
- 🔍 Memory Retrieve Tool  

### ✅ MCP‑Style Memory  
Spidey can *remember* things long‑term:

- Name  
- Preferences  
- Notes  
- Personal facts  
- Conversation history (last 5 messages)

Memory is stored in **memory.json**.

### ✅ Agent Brain (LLM‑Driven)  
Spidey uses an LLM to:

- interpret commands  
- choose correct tools  
- summarize info  
- manage context  
- do fallback chat  

Works with **Gemini**, **OpenAI**, **LLaMA**, or any LLM API.

### ✅ Kaggle-Compatible Demo  
Since Kaggle has *no microphone access*, the notebook uses:

- sample `.wav` audio commands  
- simulated STT processing  
- agent + tool execution  
- memory demonstrating updates  

### ✅ Desktop Execution  
When run locally, it uses:

- microphone input  
- app launching  
- text-to-speech output  
- real-time interaction

---

## 📁 Project Structure

assistant_spidey/
│
├── main.py # main entry: voice loop / text loop
├── agent.py # LLM agent brain + tool routing
├── tools.py # all tools (weather, wiki, search, etc.)
├── memory.py # MCP-like memory storage and retrieval
├── config.py # (optional) environment keys loader
│
├── memory.json # long-term memory
├── requirements.txt
│
├── samples/ # sample wav audio files for Kaggle
│ ├── weather.wav
│ ├── who_is_iron_man.wav
│ └── remember_name.wav
│
└── demo/
├── demo.mp4
└── demo.gif


---

## 🧠 Architecture Diagram

🎤 Voice Input (Mic or WAV)
↓
🗣 Speech-to-Text (SpeechRecognition / Vosk)
↓
🤖 LLM Agent Brain (Gemini/OpenAI)
↓
🧰 Tool Router (Gemini ADK style)
├── Weather Tool
├── Search Tool
├── Wikipedia Tool
├── App Launcher
├── Memory Add
└── Memory Get
↓
📄 Final Response Text
↓
🔊 Text-to-Speech (pyttsx3)


---

## 🛠 Installation

### 1️⃣ Clone the project
```bash
git clone https://github.com/<your-username>/assistant-spidey.git
cd assistant-spidey
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Create .env for API keys
WEATHER_API_KEY=xxxxx
GEMINI_API_KEY=xxxxx
OPENAI_API_KEY=xxxxx
▶️ Usage
🔹 Run locally (voice)
python main.py
Say commands like:

“Spidey, what’s the weather?”

“Open Chrome.”

“Remember that my name is Abhishek.”

🔹 Run in Kaggle Notebook (audio simulation)
Replace microphone input with:

text = listen_file("samples/weather.wav")
🤖 LLM Integration
Replace placeholder inside call_llm():

Gemini
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)
response = genai.GenerativeModel("gemini-1.5-pro").generate_content(prompt)
OpenAI
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(...)
🔧 Adding New Tools
Every tool is just a Python function inside tools.py.

Example:

def tool_joke():
    return "Why did the computer freeze? Because it left its Windows open!"
Add to router in agent.py:

if tool == "joke":
    return tool_joke()
🧪 Sample Commands (for WAV files)
Use these for Kaggle demo:

“What is the weather in Mumbai?”

“Who is Iron Man?”

“Remember my name is Abhishek.”

“What is my name?”

“Open Chrome.”

“Search for Spider-Man movie release date.”

🤝 Contributing
Fork the repo

Create a branch:

git checkout -b feature/new-tool
Commit:

git commit -m "Added Wikipedia detail tool"
Push:

git push origin feature/new-tool
Open Pull Request

💬 Team Collaboration
Use the GitHub:

Issues tab → track tasks

Projects Board → workflow

Pull Requests → peer review

Wiki → documentation

Branch Protection → secure main branch

📄 License
MIT License — feel free to modify, reuse, contribute.

🌐 Links
Kaggle Notebook: (add link)

Demo Video: (add link)

GitHub Repo: (add link)
