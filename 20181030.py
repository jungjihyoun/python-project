import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

search_list = ["서울시대학교", "광역시대학교", "경기도대학교", "강원도대학교", "충청도대학교", "전라도대학교", "경상도대학교", "제주도대학교"]
co_list=[]
for i in range(len(search_list)):
    print(search_list[i])
    page = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bksw&query=%s" % (search_list[i]))
    page_html = page.text
    page_soup = BeautifulSoup(page_html, "html.parser")
    name_list = page_soup.select(".lst_txt li")
    cnt = 0
    for j in range(len(name_list)):
        print(name_list[j].text.strip())
        cnt += 1
    co_list.append(cnt)
    print()

plt.bar(co_list)
plt.xlabel("college")
plt.ylabel("name")
plt.title("d")
plt.show()

