import requests
import time
from bs4 import BeautifulSoup
import pymongo


def get_page():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }

    url = "https://store.nike.com/cn/zh_cn/?ipp=120"
    response = requests.get(url, headers=header)
    return response.text


def get_02_page(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }
    url = "https://store.nike.com/html-services/gridwallData?country=CN&lang_locale=zh_CN&gridwallPath=n/1j5&pn=" + str(
        page)
    response = requests.get(url, headers=header)
    return response.json()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all(class_='grid-item-box'):
        product_name = item.find(class_='product-name')
        product_subname = item.find(class_='product-subtitle')
        local_price = item.find(class_='product-price').find(class_='local')
        bulk_pricing = item.find(class_='product-price').find(class_='bulk-pricing').attrs['data-bp']
        product = {
            '商品名称': product_name.p.string,
            '商品类别': product_subname.string,
            '原价': local_price.string,
            '员工价': bulk_pricing,
        }
        print(product)
        print('-' * 80)
        save_to_mongo(product)

# 解析ajax返回的json页面
def parse_02(html_next):
    data = html_next['sections'][0]['items']
    for item in data:
        product = {'商品名称': item['title'],
                   '商品类别': item['subtitle'],
                   '原价': item['localPrice'],
                   '员工价': item['employeePrice']
                   }
        print(product)
        print('-' * 80)
        save_to_mongo(product)

# 配置连接MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'spider_nike'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


def save_to_mongo(result):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


MAX_PAGE = 100
if __name__ == '__main__':
    # ------------ 获取数据 ---------------
    # get_page()获取不用ajax渲染的前两页数据
    html = get_page()
    # ------------ 解析数据 ---------------
    parse(html)
    print('-' * 100)
    print('-' * 100)
    time.sleep(3)
    # get_02_page()获取用ajax渲染返回的json数据
    for i in range(3, MAX_PAGE + 1):
        html_next = get_02_page(i)
        parse_02(html_next)
        print('-' * 100)
        print('-' * 100)
        # 设置睡眠时间
        # time.sleep(3)
