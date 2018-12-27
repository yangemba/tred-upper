import requests
import bs4
import random
import time
import json

wait = random.randrange(7200, 18001, 3600)
# print(wait)

with open('const.txt', 'r') as file:
    file.seek(0)
    urls = file.read()
    urls_list = urls.split(',')
    CONST1 = urls_list[0]
    CONST2 = urls_list[1]
    print(CONST1, '+' , CONST2)

with open('dict.txt', 'r') as file:
    file.seek(0)
    text = file.read()
    dict = text.split(',')
# print("dict = ", dict)

last_dict_element = (len(dict) - 1)
len_array = random.randint(0,last_dict_element)
BUMP_WORD = {

    "task" : "post",
    "board": "ch",
    "thread" : "63521",
    "usercode": None,
    "code": None,
    "captcha_type": "invisible_recaptcha",
    "email": None,
    "name": None,
    "subject" : None,
    "comment" : dict[len_array],
    "g-recaptcha-response" : None,
    "2chaptcha_id" : None

}

comment = json.dumps(BUMP_WORD)

# print("Bump-word = ", BUMP_WORD)


if __name__ == "__main__":

    while True:
        response = requests.get(CONST1)

        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            search_area = soup.findAll("div", {"class": "thread"})

            if f'thread-{CONST2}' not in str(search_area[1]):
                print("connection")
                response = requests.get(f'{CONST1}/res/{CONST2}.html')

                if response:
                    print("bump sent")
                    response = requests.post("https://2ch.hk/makaba/posting.fcgi?json=1", data = comment)
            else:
                print("Its already bumped")
        else:
            time.sleep(60)
            continue

        time.sleep(wait)

