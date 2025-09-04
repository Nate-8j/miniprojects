import json

with open("verses.json", "r", encoding="utf-8") as f:
    verses = json.load(f)

print(len(verses))