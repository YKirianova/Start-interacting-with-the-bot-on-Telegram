# Telegram Bot for Daily Reminders

This Telegram bot is designed to send daily reminders about taking vitamins.

## Features

- Sends a personalized reminder message every morning at 7 AM.
- Uses the aiogram library for Telegram bot development.
- Integrates with AsyncIOScheduler from apscheduler for scheduling tasks.

## Requirements

- Python 3.11
- aiogram
- apscheduler

## Installation

1. Set up a virtual environment and activate it:

python3 -m venv .venv
source .venv/bin/activate  # For MacOS / Linux

2. Install dependencies:
pip install aiogram apscheduler

## Usage

Replace <TOKEN> in bot.py with your Telegram bot token.

Run the bot:

python bot.py
