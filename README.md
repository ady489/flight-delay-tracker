# Flight Delay Tracker

A Python-based automation script that monitors live flight data and sends email alerts for delayed flights. 

## Why I built this
I wanted to build a practical, event-driven backend tool that solves a real problem: knowing when a flight is delayed without having to constantly refresh a website. 

## Architecture
The application is built using a modular design to separate concerns:
*   `api_client.py`: Connects to the Aviationstack API to fetch live flight data.
*   `analyzer.py`: Parses the JSON response and checks the delay status.
*   `notifier.py`: Handles SMTP email connections to send alerts.
*   `main.py`: The engine that runs the loop and ties the modules together.

## Tech Stack
*   **Language:** Python 3
*   **Libraries:** `requests`, `smtplib`, `python-dotenv`
*   **API:** Aviationstack

## How to run it locally
1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt` *(Note: I'll help you make this file next)*
5. Create a `.env` file and add your credentials:
   ```text
   AVIATIONSTACK_KEY=your_key
   EMAIL_SENDER=your_email
   EMAIL_PASSWORD=your_app_password
   EMAIL_RECEIVER=your_email
6. Run the script: python3 main.py