# AI Interview Preparation Agent

An interactive Python application that simulates a **real interview** using [CrewAI](https://github.com/joaomdmoura/crewai) and [LangChain](https://www.langchain.com/).
The agent asks job-relevant questions, listens to your answers, and follows up with new questions — helping you prepare effectively for interviews.

---

## 🚀 Features
- AI-powered interviewer agent
- Dynamic follow-up questions based on your answers
- Exit anytime with `exit`
- Powered by OpenAI's `gpt-4o-mini` model
- Extendable to record your answers for review

---

## 📦 Requirements
- Python 3.9+
- OpenAI API key

---

## 🔧 Installation

1. **Clone or copy the project**
   ```bash
   git clone https://github.com/NewtonKamau/ai_bootcamp.git
   cd ai-interview-agent
````

2. **Install dependencies**

   ```bash
   pip install langchain langchain-openai crewai ipython
   ```

3. **Set your OpenAI API key**

   On **Linux/Mac**:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

   On **Windows (PowerShell)**:

   ```powershell
   setx OPENAI_API_KEY "your_api_key_here"
   ```

---

## ▶️ Running the Interview

Run the script from your terminal:

```bash
python first_agent.py
```

Example session:

```
--- Interview Session Started ---
Type 'exit' anytime to quit.

Interviewer: Let's start. Why do you think you are a good fit for the Senior Consultant/Instructor role?
You: I have over 5 years of experience in sports program management.
Interviewer: Can you describe a specific project where you mentored athletes and improved performance?
```

Type `exit` anytime to stop the session.

---

## 📂 Project Structure

```
.
├── first_agent.py    # Main script
├── README.md       # Project instructions
```

---

## 🛠️ Customization

* Update `interviewer`, `company`, `job_position`, and `job_description` variables inside `interview.py` to tailor the interview.
* You can switch the LLM model by changing:

  ```python
  llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
  ```
* Extend `run_interview()` to save your answers to a file for later review.

---

## 📜 License

MIT License. Free to use and modify.

