import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    tag = soup.find("div",{"id":"mp-right"})
    h = tag.find_all("h2")
    content = [h.text for h in h]
    print(content)
 
    with open("wiki.csv","w") as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(content)

Extract("https://en.wikipedia.org/wiki/Main_Page")
