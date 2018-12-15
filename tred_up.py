import requests
import bs4

response = requests.get("https://2ch.hk/ch")
soup = bs4.BeautifulSoup(response.text, "html.parser")
search_area = soup.findAll("div", {"class": "thread"})

#print(search_area[1])

CONST = "thread-63521"

if CONST in str(search_area[4]):
    print("yes")
    response = requests.get("https://2ch.hk/ch/res/63521.html")
    if response:
        print("connection")