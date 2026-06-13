import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"  

url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid=bd5e378503939ddaee76f12ad7a97608&units=metric"

response = requests.get(url)

data = response.json()

temperature = data["main"]["temp"]

condition = data["weather"][0]["main"]

print("Temperature:", temperature)
print("Condition:", condition)
if temperature < 20:
    print("low Temperature Alert")

if condition == "cold":
    print("Cold Weather Alert")

import os

print("API =", os.environ.get("WEATHER_API_KEY"))
print("EMAIL =", os.environ.get("EMAIL_ADDRESS"))

sender = os.environ["EMAIL_ADDRESS"]
app_password = os.environ["EMAIL_PASSWORD"]
API_KEY = os.environ["WEATHER_API_KEY"]
import smtplib
from email.message import EmailMessage

sender = os.environ["EMAIL_ADDRESS"]
app_password = os.environ["EMAIL_PASSWORD"]

msg = EmailMessage()

msg["Subject"] = "Weather Alert"
msg["From"] = sender
msg["To"] = sender

msg.set_content(
    f"""
Weather Report

Temperature: {temperature}°C
Condition: {condition}

This is an automated weather alert.
"""
)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(sender, app_password)
    smtp.send_message(msg)

print("Email Sent Successfully!")