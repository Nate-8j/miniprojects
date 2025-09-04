import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bible.com/ru/reading-plans/40-top-verses-to-memorize/day"

verses_list = []
for i in range(1, 444):
    req = requests.get(f"{url}/{i}")
    soup = BeautifulSoup(req.text, "lxml")

    link = soup.find("a", class_="hover:no-underline items-center text-gray-50 border-gray-10 border-solid inline-flex justify-between plb-2 no-underline w-full border-b-0")
    if not link:
        continue

    link = "https://www.bible.com" + link.get("href")

    verse_link = requests.get(link)
    soup = BeautifulSoup(verse_link.text, "lxml")
    reference = soup.find("h1", class_="text-text-light dark:text-text-dark text-23 md:text-28 leading-comfy font-aktiv-grotesk bg-canvas-light plb-3 font-bold text-center w-full").text
    verse = soup.find("p", class_="text-text-light dark:text-text-dark text-17 md:text-19 leading-default md:leading-comfy font-aktiv-grotesk font-medium mbe-2").text
    print(i, reference, verse)
    if verse:
        verses_list.append({
            "reference": reference,
            "verse": verse,
        })

with open("verses.json", "w", encoding="utf-8") as file:
    json.dump(verses_list, file, ensure_ascii=False, indent=2)

print("OK!")




