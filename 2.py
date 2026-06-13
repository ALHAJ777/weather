print("program starte") 
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ---------------------------
# BBC
# ---------------------------
def get_bbc():
    url = "https://www.bbc.com/news"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    headlines = []

    for item in soup.select("h2")[:5]:
        text = item.get_text(strip=True)
        if text:
            headlines.append({
                "title": text,
                "link": url,
                "time": "Latest"
            })

    return headlines


# ---------------------------
# Reuters
# ---------------------------
def get_reuters():
    url = "https://www.reuters.com/world/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    headlines = []

    for item in soup.select("h3")[:5]:
        text = item.get_text(strip=True)
        if text:
            headlines.append({
                "title": text,
                "link": url,
                "time": "Latest"
            })

    return headlines


# ---------------------------
# AP News
# ---------------------------
def get_ap():
    url = "https://apnews.com/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    headlines = []

    for item in soup.select("h2")[:5]:
        text = item.get_text(strip=True)
        if text:
            headlines.append({
                "title": text,
                "link": url,
                "time": "Latest"
            })

    return headlines


def build_html():
    html = """
    <html>
    <body>
    <h1>📰 Daily News Digest</h1>
    """

    sources = {
        "BBC": get_bbc(),
        "Reuters": get_reuters(),
        "AP News": get_ap()
    }

    for source, news in sources.items():
        html += f"<h2>{source}</h2><ul>"

        for item in news:
            html += f"""
            <li>
            <a href="{item['link']}">{item['title']}</a>
            <br>
            Published: {item['time']}
            </li><br>
            """

        html += "</ul>"

    html += "</body></html>"

    return html
from dotenv import load_dotenv
load_dotenv()


def send_email(html_content):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("TO_EMAIL")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Daily News Digest"
    msg["From"] = sender
    msg["To"] = receiver

    msg.attach(MIMEText(html_content, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    server.sendmail(sender, receiver, msg.as_string())

    server.quit()


if __name__ == "__main__":
    print("Building HTML...")
    html = build_html()

    print("Sending Email...")
    send_email(html)

    print("Done")
