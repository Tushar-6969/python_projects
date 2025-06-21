# 🎹 Python Voice Assistant - Jarvis

A simple voice-controlled virtual assistant built using Python. It can recognize your speech, respond with voice output, and perform various tasks like telling time, opening YouTube, telling jokes, searching Google, and playing local music.

---

## 💡 Features

* 🔊 Text-to-Speech using `pyttsx3`
* 🎤 Speech Recognition using `speech_recognition`
* 🌐 Google search on voice command
* ⏰ Tell current time
* 🎵 Play music from local directory
* 📺 Open YouTube in browser
* 🤣 Speak neutral jokes using `pyjokes`
* 🗣 Conversational responses (name, age, etc.)

---

## 🧪 Requirements

Install dependencies using pip:

```bash
pip install pyttsx3 SpeechRecognition pyjokes requests
```

Also install:

* `pyaudio` (required by `speech_recognition`)

> ⚠️ On Windows, install PyAudio with:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🚀 How to Run

1. Ensure your microphone is working.
2. Save the Python code as `jarvis.py` (or any filename).
3. Run the script:

```bash
python jarvis.py
```

Then say things like:

* “What’s the time?”
* “Open YouTube”
* “Search Python projects”
* “Tell me a joke”
* “Play song”
* “Exit”

---

## 📁 Customization

* **Change music directory:** Update this line:

  ```python
  add = r"C:\Users\Tushar\Music"
  ```
* **Switch to female voice:**

  ```python
  engine.setProperty('voice', voices[1].id)
  ```

---

## 👨‍💼 Author

**Tushar Rathor**
BTech CSE (AIML) Student
GitHub: [@Tushar-6969](https://github.com/Tushar-6969)

---

## ⭐ Like this?

If you find this project useful or fun, consider giving it a ⭐ on GitHub!
