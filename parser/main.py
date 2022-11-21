from bs4 import BeautifulSoup
import requests
import pandas as pd

def parse(token, version, group_id, sort):
    response = requests.get("https://api.vk.com/method/groups.getMembers",
                            params={
                                "access_token": token,
                                "v": version,
                                "group_id": group_id,
                                "offset": 100,
                                "count": 10
                            })
    data = response.json()
    df = pd.DataFrame()
    names = []
    ids = []
    k = 0
    print(data)
    for i in data["response"]["items"]:
        link = "https://vk.com/id" + str(i)
        # print(link)

        html = requests.get(link)
        print(k)
        content = html.content
        soup = BeautifulSoup(content, "lxml")
        k += 1
        if soup.find("h2", class_="op_header"):
            item = soup.find("h2", class_="op_header").text
            ids.append(i)
            names.append(item)
    print("all")
    data_pages = {"id": ids, "Name": names}
    df = pd.DataFrame(data_pages)
    df.to_excel('./names.xlsx')