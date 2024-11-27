import requests
from bs4 import BeautifulSoup
from sender import send_email
from recvier import recvier_emails

# 要爬取的目標網址
URL = "https://www.csie.ncu.edu.tw/"
CHECKED = "checked_links"

# 讀取已檢查過的消息
def load_checked_items():
    try:
        with open(CHECKED, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()
    
# 儲存已檢查過的消息
def save_checked_items(checked_links):
    with open(CHECKED, "w") as file:
        for href in checked_links:
            file.write(f"{href}\n")

# 爬取網頁內容
def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('article')

# 爬取消息
def fetch_news():
    checked_items = load_checked_items()
    new_checked_items = set()
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    announcement_scope = soup.find('div', {'class': 'announcement-scope', 'data-scope-tag': '招生快訊'})

    if announcement_scope:
        links = announcement_scope.find_all('a', {'class': 'link'})
        for link in links:
            href = link.get('href')
            title = link.get('title')
            
            new_checked_items.add(href)
            if href in checked_items:
                continue

            # 結果
            # link = URL[:-1]+href
            # print(f"連結: {link}")
            # print(f"標題: {title}")
            # # print(fetch_content(link))
            # print("-" * 30)
            
            for recvier_email in recvier_emails:
                send_email(fetch_content(link), recvier_email, title, "中央爬蟲通知")
    else:
        print("未找到目標範圍")

    save_checked_items(new_checked_items)

if __name__ == "__main__":
    fetch_news()
