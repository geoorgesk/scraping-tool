import requests
from bs4 import BeautifulSoup

url = "https://www.thefactsite.com/soccer-facts/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Get all <p class="list"> elements
facts = soup.find_all("p", class_="list")

# Save facts to a text file
with open("football_facts.txt", "w", encoding="utf-8") as f:
    for i, fact in enumerate(facts, 1):
        text = fact.get_text().strip()
        if text:
            f.write(f"{i}. {text}\n")

print("✅ Facts saved to football_facts.txt")
