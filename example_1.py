# https://stackoverflow.com/a/68191523

from bs4 import BeautifulSoup
import requests

url = requests.get("https://realpython.com/atom.xml")

soup = BeautifulSoup(url.content, "xml")
entries = soup.find_all("entry")

entry_list = list()

for entry in entries:
    title = entry.title.text
    link = entry.link["href"]
    summary = entry.summary.text
    __str__ = ("Title: {title}\n\tSummary: {summary}\n\tURL: {link}\n\n"
        .format(title=title, summary=summary, link=link))
    entry_list.append({
        "title": title,
        "url": link,
        "summary": summary,
        "display": __str__
        })
    print(__str__)
