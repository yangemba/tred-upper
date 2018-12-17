import requests
import bs4
import random
import time

wait = random.randrange(7200, 18001, 3600)
# print(wait)

with open('const.txt', 'r') as file:
    file.seek(0)
    CONST = file.read()
# print("const = ", CONST)

with open('dict.txt', 'r') as file:
    file.seek(0)
    text = file.read()
    dict = text.split(',')
# print("dict = ", dict)

last_dict_element = (len(dict) - 1)
len_array = random.randint(0,last_dict_element)
BUMP_WORD = dict[len_array]
# print("Bump-word = ", BUMP_WORD)

while True:
    response = requests.get("https://2ch.hk/ch")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        search_area = soup.findAll("div", {"class": "thread"})

        if CONST not in str(search_area[1]):
            print("connection")
            response = requests.get("https://2ch.hk/ch/res/63521.html")

            if response:
                print("sent bump")
                response = requests.post("https://2ch.hk/makaba/posting.fcgi?json=1", data = BUMP_WORD)
        else:
            print("Its already bumped")
    else:
        continue
    time.sleep(wait)
