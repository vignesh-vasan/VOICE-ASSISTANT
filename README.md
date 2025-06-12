🎙️ Python Voice Assistant

A powerful and extensible voice-controlled assistant built in Python that can handle tasks like:

* Answering general questions via **Wikipedia**
* Performing **computations** with **WolframAlpha**
* Fetching **weather** details using OpenWeatherMap
* Opening **websites**, telling the **date/time**, and more!

---

📦 Features

* 🎤 **Voice Recognition** using Google Speech Recognition
* 🔊 **Text-to-Speech** using `pyttsx3`
* 📚 **Wikipedia** summary search
* 🌦️ **Real-time Weather** updates using OpenWeatherMap API
* 🧠 **Computational Intelligence** via WolframAlpha
* 🌐 **Open websites** using voice commands
* 🕓 **Date and Time** reporting
* 🛑 Graceful **shutdown** via voice

---

🧰 Requirements

Install the required packages using pip:

```bash
pip install speechrecognition pyttsx3 wikipedia wolframalpha requests
```

Also install additional dependencies for `speech_recognition`:

* On Windows: [Install PyAudio wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
* On Linux/macOS: `sudo apt install portaudio19-dev` then `pip install pyaudio`

---

 🔐 API Keys Required

Before running the script, replace the placeholders in your code:

```python

* 🔑 [WolframAlpha API Key](https://developer.wolframalpha.com/portal/myapps/)
* 🌦️ [OpenWeatherMap API Key](https://home.openweathermap.org/users/sign_up)

---

🚀 How to Run

```bash
python your_script_name.py
```

Your assistant will greet you and start listening for commands like:

* `"What's the time?"`
* `"Tell me about Albert Einstein on Wikipedia"`
* `"Open website YouTube"`
* `"What’s the weather in London?"`
* `"Calculate 12 divided by 3"`
* `"Exit"`

---

## 💡 Example Commands

| 🗣️ Command              | 🤖 Action                                |
| ------------------------ | ---------------------------------------- |
| `"Hello"`                | Greets back                              |
| `"Time"`                 | Tells current time                       |
| `"Date"`                 | Tells current date                       |
| `"Wikipedia"`            | Asks and summarizes topic from Wikipedia |
| `"Weather"`              | Prompts for city and returns forecast    |
| `"Open website YouTube"` | Opens `https://www.youtube.com`          |
| `"Calculate 2 plus 2"`   | Returns computational result             |
| `"Exit"`                 | Stops the assistant                      |

---

## 🛠 Future Enhancements

* Add task scheduling (reminders)
* Add music player integration
* Integrate with GPT APIs for smart Q\&A
* GUI for better interaction

---

## 👨‍💻 Author

Developed by **\vignesh-vasan**
Feel free to fork, improve, and contribute!


