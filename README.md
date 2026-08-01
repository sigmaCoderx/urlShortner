# Telegram URL Shortener & Admin Management Bot

A feature-rich Telegram bot built with Python (`pyTelegramBotAPI`), `pyshorteners`, and MongoDB. It automatically converts long links into multiple shortened formats simultaneously, enforces channel subscription, and includes an admin system with database storage.

---

## Features

- **Multi-Service URL Shortening:** Generates multiple short links at once using TinyURL, Clck.ru, Is.gd, Os.db, and Lnk.pw.
- **URL Validation:** Validates input URLs using `pyLense` before attempting to shorten them.
- **Force Subscription Gate:** Ensures users are subscribed to a required update channel before accessing bot features.
- **MongoDB Integration:** Automatically tracks user profiles and stores admin roles using PyMongo.
- **Admin Dashboard & Tools:**
  - `/broadcast`: Send global messages to all registered users in the database.
  - `/notify`: Send targeted direct messages to specific users via their Telegram ID.
  - `/adminreg`: Register new administrative users with custom permissions into MongoDB.
  - `/totaluser`: View live user count metrics stored in the database.

---

## Prerequisites

- **Python 3.x** installed.
- **MongoDB instance** (MongoDB Atlas cluster or local MongoDB service).
- A **Telegram Bot Token** from [@BotFather](https://t.me/BotFather).

---

## Setup & Installation

1. Clone or download this repository.
2. Install the required Python packages:

   ```bash
   pip install pyTelegramBotAPI requests pyshorteners pymongo pyLense
