# Lia_Plus_Chatbot
Created a Chatbot with Sentiment Analysis
# Chatbot With Sentiment Analysis  
### Tier 1 (Mandatory) + Tier 2 (Optional Enhancement)

This project implements a Python-based conversational chatbot capable of performing **sentiment analysis** on user input. The chatbot supports two modes:

- **Tier 1 – Conversation-Level Sentiment Analysis (Mandatory)**  
- **Tier 2 – Statement-Level Sentiment Analysis (Optional, Extra Credit)**  

The system maintains full conversation history, analyzes user sentiment, and generates an emotional summary.

---

## 📌 Features

### ✔ Tier 1 – Conversation-Level Sentiment
- Tracks every user message.
- Computes overall sentiment score for the **entire conversation**.
- Classifies the conversation as **Positive, Neutral, or Negative**.
- Shown automatically when the chat session ends.

### ✔ Tier 2 – Statement-Level Sentiment (Bonus)
- Evaluates sentiment for **each user message individually**.
- Shows sentiment category + numerical score.
- Detects **mood shift across conversation** (e.g., “Improving mood”).

### ✔ Chatbot Functionality
- Maintains conversation history.
- Responds using simple rule-based logic.
- Handles problem-related, gratitude, and general messages.
- Clean, modular code (Chatbot class + SentimentAnalyzer class).

---

## 📁 Project Structure

Chatbot/
│── main.py # Runs the chatbot and manages I/O
│── sentiment.py # Sentiment analysis logic (Tier 1 & Tier 2)
│── run_tests.py # Optional tests if implemented
│── README.md # Documentation


---

## 🚀 How to Run the Project

### ▶ 1. Install dependencies
Your project uses only Python standard libraries, so no special installation is required.

If your sentiment analyzer uses `textblob` or `vaderSentiment`, install it:


---

## 🧠 Sentiment Logic Explained

The sentiment module performs:

### ✔ **Statement-Level Sentiment (Tier 2)**
Each message is scored in the range:
- **Negative** < 0  
- **Neutral** = 0  
- **Positive** > 0  

### ✔ **Conversation-Level Sentiment (Tier 1)**
- Computes the **average sentiment score** across all user messages.
- Assigns an overall label:
  - Positive  
  - Neutral  
  - Negative  

### ✔ **Mood Trend (Optional Bonus)**
Compares the first and last message scores:
- Improving mood  
- Declining mood  
- No significant change  

## 🧪 Example Output

User: Your service disappoints me
Bot: I'm sorry you're having issues — can you describe the problem?

User: Last experience was better
Bot: Thanks for telling me. Could you say more?

User: Thanks
Bot: You're welcome! Anything else I can help with?

exit

---

## 🧪 Tests (If Included)
The repository may optionally contain:
- `run_tests.py`
- Test cases for the sentiment analyzer
- Test cases for chatbot interaction logic

(If you include tests, describe them here.)

---

## ✨ Optional Enhancements Implemented
- Trend summary for emotional shift.
- Modular, reusable class design.
- Rule-based response system.

---

## 👤 Author
**Krishnadwaipayen Ghosh**  
Chatbot + Sentiment Analysis Assignment (Module-Based)

---

## 📄 License
This project is for academic use only.

