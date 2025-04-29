# 💡 MotiBot for Microsoft Teams — Daily Motivation in Your Channel

> ✨ Boost team morale with a daily motivational quote — directly in Microsoft Teams.

---

## 📌 What It Does

MotiBot automatically sends a motivational quote every day at 05:00 PM to a Microsoft Teams channel via an Incoming Webhook or Bot Framework integration.
It's simple, inspiring, and perfect for energizing distributed teams.


---

## 🌟 Example Message

> ✨ **Daily Motivation** ✨
>
> *"Fears are nothing more than a state of mind."*
>
> — *Napoleon Hill*

---

## 🧰 Tech Stack

- Python 3.10+
- [Requests](https://pypi.org/project/requests/)
- [ZenQuotes API](https://zenquotes.io/)
- Microsoft Teams Incoming Webhook (or Bot Framework)
- [Schedule](https://pypi.org/project/schedule/)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SP-Satiato/motivation-bot.git
cd motivation-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
Put your Microsoft Teams Incoming Webhook or Bot Framework URL in the .env file.
```

### 4. Run the Script

```bash
python teams_bot.py
```
