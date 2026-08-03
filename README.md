# 🔗 URL Shortener Telegram Bot

A Telegram bot built with Python that shortens URLs using multiple URL shortening services. Simply send a valid URL, and the bot instantly returns several shortened versions from different providers.

The bot also includes user management, force subscription, broadcasting, admin tools, and MongoDB integration.

---

## Features

- 🔗 Shorten URLs using multiple providers
- ⚡ Generate multiple shortened links instantly
- 👥 User registration with MongoDB
- 📢 Broadcast messages to all users
- 📩 Send notifications to specific users
- 🔐 Admin-only commands
- 📊 View total registered users
- ✅ URL validation before shortening
- 📌 Force users to join a Telegram channel

---

## Supported URL Shorteners

- TinyURL
- Clck.ru
- is.gd
- osdb
- lnk.pw
- Bitly (API supported)

---

## Tech Stack

- Python
- pyTelegramBotAPI
- MongoDB
- PyMongo
- Requests
- pyshorteners
- pyLense

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/urlShortner.git
cd urlShortner
```

### Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the bot, replace the placeholders inside the source code.

### Telegram Bot Token

```python
<BOT API TOKEN>
```

Create one using:

https://t.me/BotFather

---

### MongoDB Connection

```python
<MONGODB URL>
```

Replace it with your MongoDB Atlas or local MongoDB connection string.

---

### Bitly API Key (Optional)

```python
API_KEY
```

Only required if you plan to use Bitly shortening.

---

### Force Subscription

Update the Telegram channel username if needed.

```python
@Neuralp
```

---

## Running the Bot

```bash
python urshortBeta.py
```

---

## Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot |
| `/broadcast` | Broadcast a message to every user *(Admin)* |
| `/notify` | Send a message to a specific user *(Admin)* |
| `/adminreg` | Register a new admin *(Admin)* |
| `/totaluser` | Display total registered users |

---

## How It Works

1. Start the bot.
2. Join the required Telegram channel.
3. Send any valid URL.
4. The bot validates the URL.
5. Multiple shortened links are generated.
6. Copy and use whichever link you prefer.

---

## Example

### Input

```
https://github.com/sigmaCoderx
```

### Output

```
https://tinyurl.com/...

https://clck.ru/...

https://is.gd/...

https://osdb.link/...

https://lnk.pw/...
```

---

## Project Structure

```
urlShortner/
├── urshortBeta.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

All project dependencies are listed in **requirements.txt**.

Install them with:

```bash
pip install -r requirements.txt
```

---

## Notes

- Requires a valid Telegram Bot Token.
- Requires a MongoDB database.
- Requires an internet connection.
- Some URL shortening services may enforce rate limits or become unavailable.
- Never commit your Bot Token, MongoDB URI, or API keys to GitHub.

---

## Future Improvements

- QR code generation
- URL analytics
- Custom aliases
- Click tracking
- User dashboard
- Expiring short links
- REST API support

---

## License

MIT License

---

## Author

**flippedCoin**

GitHub: https://github.com/sigmaCoderx

---

⭐ If you found this project useful, consider giving it a star on GitHub.
