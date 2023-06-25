import requests
from bs4 import BeautifulSoup

# 定義網頁URL
url = "https://www.wantgoo.com/stock/1514/technical-chart"

# 發送GET請求獲取網頁內容
response = requests.get(url)

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(response.text, "html.parser")

# 找到蠟燭線數據所在的HTML元素，並提取相關資訊
candlestick_data = soup.find("div", class_="cstick-chart").find_all("div", class_="cstickdata")

# 將蠟燭線數據轉換成字典格式
candlestick_dict = {}
for data in candlestick_data:
    time = data["data-time"]
    open_price = data["data-open"]
    high_price = data["data-high"]
    low_price = data["data-low"]
    close_price = data["data-close"]
    candlestick_dict[time] = {
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price
    }

# 輸出蠟燭線字典
#print(candlestick_dict)
print(soup.prettify())
