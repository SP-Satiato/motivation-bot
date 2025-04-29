import os

import requests
from dotenv import load_dotenv

load_dotenv()

TEAMS_WEBHOOK_URL = os.environ['TEAMS_WEBHOOK_URL']


def post_to_teams(text, author):
    payload = {
        "text": f"✨ *Daily Motivation* ✨\n\n> {text}\n\n— *{author}*"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(TEAMS_WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")


def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        return data['q'], data['a']
    except Exception:
        return "Keep pushing forward! 🚀", "Unknown"


def send_motivation():
    quote, author = get_motivational_quote()
    post_to_teams(quote, author)


if __name__ == "__main__":
    send_motivation()
