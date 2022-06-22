import requests
from bs4 import BeautifulSoup

SUBJECT = "Scrapping".replace(" ", "%20")
print(SUBJECT)
# codigo para get principais noticias no google

print("Googgle Search\n")
URL = f"https://www.google.com/search?q={SUBJECT}&ei=9uiyYuiqPIv41sQPpd29yA8&ved=0ahUKEwjo_Yqa58D4AhULvJUCHaVuD_kQ4dUDCA4&uact=5&oq=manha+perfeita&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABKBAhGGABQAFgAYNUIaANwAXgAgAEAiAEAkgEAmAEAyAEIwAEB&sclient=gws-wiz"
response = requests.get(URL, headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'})
soup = BeautifulSoup(response.content, "html.parser")
news = soup.find_all("div", attrs={"class":"g tF2Cxc"})

for new in news:
    print(" ".join(new.h3.text.split()), "\n")
    print(new.a["href"])
    print()

# Get 4 noticies in google news
print("\n",60*"-","\n")
print("Google News\n")

INDICE = 0
PAGES = 1
COUNT = 0
for i in range(PAGES):
    URL2 = f"https://www.google.com/search?q={SUBJECT}&hl=pt-BR&tbm=nws&ei=x-GyYqCFNPjk1sQP5927gAQ&start={INDICE}&sa=N&ved=2ahUKEwjghI-t4MD4AhV4spUCHefuDkA4ChDy0wN6BAgBEDw&biw=948&bih=730&dpr=2"
    response2 = requests.get(URL2, headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    })
    soup2 = BeautifulSoup(response2.content, "html.parser")

    news2 = soup2.find_all("div", attrs={"class":"xuvV6b BGxR7d"})
    INDICE += 10

    for new in news2:
        print(" ".join(new.find("div", attrs={"class": "mCBkyc y355M ynAwRc MBeuO nDgy9d"}).text.split()), "\n")
        # print(" ".join(new.text.split()), "\n")
        print(new.a["href"])
        print()

    COUNT += len(news2)

print("Content: ", COUNT)
