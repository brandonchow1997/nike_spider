import requests
import time
from bs4 import BeautifulSoup
import pymongo


def get_page():
    header = {
        'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti1; adfcid2=pzzhubiaoti1; adfbid=0; adfbid2=0; sts_deviceid=164b708c726141-0b5a721fc-3b444329-1049088-164b708c729a9; sts_sg=1; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D25017023_5_dg%26ch%3D1%26ie%3DUTF-8%26wd%3Dzhilianzhaopin; dywez=95841923.1532079163.3.3.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=zhilianzhaopin; __xsptplus30=30.1.1532079163.1532079163.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23M1CLi7jG6OM2mDiY8ntZv60N-ySC4BGh%23; __utmt=1; _jzqy=1.1526643282.1532079164.2.jzqsr=baidu.jzqsr=baidu|jzqct=zhilianzhaopin; _jzqckmp=1; qrcodekey=b0d72e663d784ceeb83d1db22b23aeda; _jzqa=1.2278863967071744800.1515904529.1526643282.1532079164.3; _jzqc=1; _jzqb=1.2.10.1532079164.1; firstchannelurl=https%3A//passport.zhaopin.com/login%3Fy7bRbP%3DdpodqL8ofg8ofg8oScnqZCnf748SEa5JdFDBb8XLuLQ; lastchannelurl=https%3A//passport.zhaopin.com/login; JsNewlogin=2123451650; JSloginnamecookie=13500732402; JSShowname=%E6%AD%A6%E7%91%9E%E9%B9%8F; at=15f0f1390d9c48d2b334f47174d1cf8e; Token=15f0f1390d9c48d2b334f47174d1cf8e; rt=b90230de76944924ae3ae9a1a6953571; JSsUserInfo=3d692e695671407155775e75516a557547775a695b695d714c7129772775546a557543775d695a695b71407156775b755d6a5475427753693f6925714a71031c370126f45f753577256957691b7112710b770e751b6a117519775d695f695e71427150772975586a527543774669096904711a715e773a753d6a5975417753692b693f714a71537744755c6a447541775f695069587144715e772875256a5975407753693f692a714a712f772575596a5375487759695d695971467153775e75526a3175247755695b69507124712c775475586a5f7525773869246956710771007707750e6a1675057701695f695e71427150775c75296a557546775b69446908711871087752756; uiioit=3b622a6459640f644764406a506e536e536456385577527751682c622a64596408644c646; dywea=95841923.3780843914165976000.1515904529.1526643281.1532079163.3; dywec=95841923; dywem=95841923.y; dyweb=95841923.3.10.1532079163; __utma=269921210.47306283.1515904529.1526643282.1532079164.3; __utmb=269921210.3.10.1532079164; __utmc=269921210; __utmz=269921210.1532079164.3.3.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=zhilianzhaopin; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1532079164; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1532079455; sts_evtseq=16; sts_sid=164b708c7312e3-0cae6079e-3b444329-1049088-164b708c732a8; ZP_OLD_FLAG=false; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; GUID=4833c4700857470ba3af93383fe4e817; ZL_REPORT_GLOBAL={%22//i%22:{%22actionIdFromI%22:%22b900c1f6-9ccc-4d87-9ab0-ff540a80a7f2-i%22}%2C%22sou%22:{%22actionIdFromSou%22:%22a95383de-4500-4c38-b773-576e1480a36e-sou%22%2C%22funczone%22:%22smart_matching%22}}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453'
    }

    url = "https://store.nike.com/cn/zh_cn/?ipp=120"
    response = requests.get(url, headers=header)
    return response.text


def get_02_page(page):
    header = {
        'Cookie': 'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti1; adfcid2=pzzhubiaoti1; adfbid=0; adfbid2=0; sts_deviceid=164b708c726141-0b5a721fc-3b444329-1049088-164b708c729a9; sts_sg=1; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D25017023_5_dg%26ch%3D1%26ie%3DUTF-8%26wd%3Dzhilianzhaopin; dywez=95841923.1532079163.3.3.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=zhilianzhaopin; __xsptplus30=30.1.1532079163.1532079163.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23M1CLi7jG6OM2mDiY8ntZv60N-ySC4BGh%23; __utmt=1; _jzqy=1.1526643282.1532079164.2.jzqsr=baidu.jzqsr=baidu|jzqct=zhilianzhaopin; _jzqckmp=1; qrcodekey=b0d72e663d784ceeb83d1db22b23aeda; _jzqa=1.2278863967071744800.1515904529.1526643282.1532079164.3; _jzqc=1; _jzqb=1.2.10.1532079164.1; firstchannelurl=https%3A//passport.zhaopin.com/login%3Fy7bRbP%3DdpodqL8ofg8ofg8oScnqZCnf748SEa5JdFDBb8XLuLQ; lastchannelurl=https%3A//passport.zhaopin.com/login; JsNewlogin=2123451650; JSloginnamecookie=13500732402; JSShowname=%E6%AD%A6%E7%91%9E%E9%B9%8F; at=15f0f1390d9c48d2b334f47174d1cf8e; Token=15f0f1390d9c48d2b334f47174d1cf8e; rt=b90230de76944924ae3ae9a1a6953571; JSsUserInfo=3d692e695671407155775e75516a557547775a695b695d714c7129772775546a557543775d695a695b71407156775b755d6a5475427753693f6925714a71031c370126f45f753577256957691b7112710b770e751b6a117519775d695f695e71427150772975586a527543774669096904711a715e773a753d6a5975417753692b693f714a71537744755c6a447541775f695069587144715e772875256a5975407753693f692a714a712f772575596a5375487759695d695971467153775e75526a3175247755695b69507124712c775475586a5f7525773869246956710771007707750e6a1675057701695f695e71427150775c75296a557546775b69446908711871087752756; uiioit=3b622a6459640f644764406a506e536e536456385577527751682c622a64596408644c646; dywea=95841923.3780843914165976000.1515904529.1526643281.1532079163.3; dywec=95841923; dywem=95841923.y; dyweb=95841923.3.10.1532079163; __utma=269921210.47306283.1515904529.1526643282.1532079164.3; __utmb=269921210.3.10.1532079164; __utmc=269921210; __utmz=269921210.1532079164.3.3.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=zhilianzhaopin; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1532079164; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1532079455; sts_evtseq=16; sts_sid=164b708c7312e3-0cae6079e-3b444329-1049088-164b708c732a8; ZP_OLD_FLAG=false; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; GUID=4833c4700857470ba3af93383fe4e817; ZL_REPORT_GLOBAL={%22//i%22:{%22actionIdFromI%22:%22b900c1f6-9ccc-4d87-9ab0-ff540a80a7f2-i%22}%2C%22sou%22:{%22actionIdFromSou%22:%22a95383de-4500-4c38-b773-576e1480a36e-sou%22%2C%22funczone%22:%22smart_matching%22}}',
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
        time.sleep(3)
