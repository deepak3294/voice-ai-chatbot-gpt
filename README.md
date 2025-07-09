# 🎓 AI Chatbot with GPT Fallback – Voice-Based University Assistant

An intelligent voice-enabled chatbot built in Python that answers predefined university-related queries (like admission, courses, fees) and uses **GPT4All** to handle anything beyond its built-in knowledge. Think of it as your academic buddy — fast, informative, and smart.



## 💡 Features

- 🧠 **Predefined answers** to university FAQs (admissions, fees, courses, etc.)
- 🤖 **Fallback to GPT4All** for unknown or general queries
- 🎤 **Voice-controlled interface** using SpeechRecognition
- 🔈 **Text-to-speech replies** via gTTS and Pygame
- 🌐 Auto-launches admission portal for application-related queries
- ⚡ Works offline (GPT4All model is local)
- 🏫 Focused on Indian university context (DCRUST)



## 📁 Project Structure
├── main.py         # Main chatbot script with voice interaction
├── gpt.py          # Loads GPT4All language model safely
├── qa.py           # Contains predefined university questions & responses



🛠️ Technologies Used
Python 3
gTTS (Google Text-to-Speech)
SpeechRecognition
Pygame
GPT4All (LLM)
Webbrowser
Socket (for internet checks)



🚀 How to Run
1. Install dependencies:
pip install gtts pygame SpeechRecognition gpt4all
2. Download your GPT4All model
Place the model file (e.g. orca-mini-3b-gguf2-q4_0.gguf) in your working directory.
3. Run the assistant:
python main.py
Say the trigger word: tiny
Then ask any university or academic-related question by voice.



🧠 Sample Questions It Can Answer
"What is the last date for admission?"
"Is scholarship available?"
"What is the annual fee for BTech?"
"When will the academic session begin?"
- If it doesn’t match any built-in question, it will reply via GPT.



📸 Screenshot / Demo 
AI chatbot working screencshot you may use to check(""C:\Users\HP\OneDrive\Pictures\Screenshots\Screenshot 2025-07-09 170820.png")

📄 License
This project is open-source under the MIT License

👤 Author
Deepak Ladwal
GitHub: @deepak3294


