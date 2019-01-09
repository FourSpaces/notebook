# -*- coding:utf-8 -*-


# 这里对百度APP 进行抓包和反编译，获取接口数据

"""
# 获取店铺列表

url: http://client.waimai.baidu.com/shopui/na/v1/cliententry?resid=1001&from=na-android&os=4.4.4&sv=3.8.1&cuid=F5F020BA348E02E249827BB426C2740E%7C317570520224668&model=vivoY13L&screen=480*854&channel=com.xiazaiyewaimai&loc_lat=4828814.459516&loc_lng=1.296978134979E7&city_id=131&address=%E5%85%AB%E9%87%8C%E5%BA%84%E5%8C%97%E9%87%8C%E5%B0%8F%E5%8C%BA&net_type=wifi&isp=&request_time=1520323039587
url: http://client.waimai.baidu.com/shopui/na/v1/cliententry?resid=1001&from=na-android&os=4.4.4&sv=3.8.1&cuid=F5F020BA348E02E249827BB426C2740E%7C317570520224668&model=vivoY13L&screen=480%2A854&channel=com.xiazaiyewaimai&loc_lat=4828814.459516&loc_lng=1.296978134979E7&city_id=131&address=%E5%85%AB%E9%87%8C%E5%BA%84%E5%8C%97%E9%87%8C%E5%B0%8F%E5%8C%BA&net_type=wifi&isp=&request_time=1520323039587
#### Query String

resid	1001
from	na-android
os	4.4.4
sv	3.8.1
cuid	F5F020BA348E02E249827BB426C2740E|317570520224668
model	vivoY13L
screen	480*854
channel	com.xiazaiyewaimai
loc_lat	4828814.459516
loc_lng	1.296978134979E7
city_id	131
address	八里庄北里小区
net_type	wifi
isp
request_time	1520323039587

#### Cookies
WMST	1520322442
BAIDUID	4924530A6B242C9D17B83A1FD2786386:FG=1
WMID	db6127cd3ab2ae4944a97cbbfec2b1bc

#### text/body
lat=4828814.459516&lng=1.296978134979E7&count=20&page=2&bduss=NA&stoken=bdwm&sortby=&taste=&city_id=131&promotion=&return_type=paging

lat	4828814.459516
lng	1.296978134979E7
count	20
page	2
bduss	NA
stoken	bdwm
sortby
taste
city_id	131
promotion
return_type	paging


#### headers
	POST /shopui/na/v1/cliententry?resid=1001&from=na-android&os=4.4.4&sv=3.8.1&cuid=F5F020BA348E02E249827BB426C2740E%7C317570520224668&model=vivoY13L&screen=480*854&channel=com.xiazaiyewaimai&loc_lat=4828814.459516&loc_lng=1.296978134979E7&city_id=131&address=%E5%85%AB%E9%87%8C%E5%BA%84%E5%8C%97%E9%87%8C%E5%B0%8F%E5%8C%BA&net_type=wifi&isp=&request_time=1520323039587 HTTP/1.1
Content-Type	application/x-www-form-urlencoded
Content-Length	133
Host	client.waimai.baidu.com
Connection	Keep-Alive
Accept-Encoding	gzip
Cookie	WMST=1520322442; BAIDUID=4924530A6B242C9D17B83A1FD2786386:FG=1; WMID=db6127cd3ab2ae4944a97cbbfec2b1bc
User-Agent	okhttp/3.2.0

#### 'bdwm://native?pageName=shopMenu&shopId=1606964394'


# 获取详情
URL: http://client.waimai.baidu.com/shopui/na/v1/shopmenu?resid=1001&from=na-android&os=4.4.4&sv=3.8.1&cuid=F5F020BA348E02E249827BB426C2740E%7C317570520224668&model=vivoY13L&screen=480*854&channel=com.xiazaiyewaimai&loc_lat=4828814.459516&loc_lng=1.296978134979E7&city_id=131&address=%E5%85%AB%E9%87%8C%E5%BA%84%E5%8C%97%E9%87%8C%E5%B0%8F%E5%8C%BA&net_type=wifi&isp=&utm_source=waimai&utm_medium=shoplist&utm_content=default&utm_term=default&utm_campaign=default&cid=988272&request_time=1520327758166

#### Query String
resid	1001
from	na-android
os	4.4.4
sv	3.8.1
cuid	F5F020BA348E02E249827BB426C2740E|317570520224668
model	vivoY13L
screen	480*854
channel	com.xiazaiyewaimai
loc_lat	4828814.459516
loc_lng	1.296978134979E7
city_id	131
address	八里庄北里小区
net_type	wifi
isp
utm_source	waimai
utm_medium	shoplist
utm_content	default
utm_term	default
utm_campaign	default
cid	988272
request_time	1520327758166

#### Cookies
WMST	1520322442
BAIDUID	4924530A6B242C9D17B83A1FD2786386:FG=1
WMID	db6127cd3ab2ae4944a97cbbfec2b1bc

#### Text/from
lat	4828814.459516
lng	1.296978134979E7
shop_id	1606964394
bduss	NA
stoken	bdwm
key	O%5CFTSTDTT%5CMX%21W3%2F%23%25N%5B%21%26O%5EUPBXV%26O%28VS5.P%273TTRN%11S%5DN%5DPWEXRWEXUQDWSPD%5DQTF%5DTT
    O%5CFTSTDTT%5CMX%21W3%2F%23%25N%5B%21%26O%5EUPBXV%26O%28VS5.P%273TTRN%11S%5DN%5DPWEXRWEXUQDWSPD%5DQTF%5DTT

#### headers
	POST /shopui/na/v1/shopmenu?resid=1001&from=na-android&os=4.4.4&sv=3.8.1&cuid=F5F020BA348E02E249827BB426C2740E%7C317570520224668&model=vivoY13L&screen=480*854&channel=com.xiazaiyewaimai&loc_lat=4828814.459516&loc_lng=1.296978134979E7&city_id=131&address=%E5%85%AB%E9%87%8C%E5%BA%84%E5%8C%97%E9%87%8C%E5%B0%8F%E5%8C%BA&net_type=wifi&isp=&utm_source=waimai&utm_medium=shoplist&utm_content=default&utm_term=default&utm_campaign=default&cid=988272&request_time=1520327758166 HTTP/1.1
Content-Type	application/x-www-form-urlencoded
Content-Length	226
Host	client.waimai.baidu.com
Connection	Keep-Alive
Accept-Encoding	gzip
Cookie	WMST=1520322442; BAIDUID=4924530A6B242C9D17B83A1FD2786386:FG=1; WMID=db6127cd3ab2ae4944a97cbbfec2b1bc
User-Agent	okhttp/3.2.0

"""

import requests
import time
from urllib.parse import urlencode


def get_shop_list():
    """
    获取店铺列表
    :return:
    """
    url = "http://client.waimai.baidu.com/shopui/na/v1/cliententry?{}"

    url_data = {
        # 'resid': '1001',
        'from': 'na-android',
        'os': '4.4.4',
        'sv': '3.8.1',
        'cuid': 'F5F020BA348E02E249827BB426C2740E|317570520224668',  # 模拟格式随便填
        'model': 'vivoY13L',
        'screen': '480*854',
        'channel': 'com.xiazaiyewaimai',
        'loc_lat': '4828814.459516',
        'loc_lng': '1.296978134979E7',
        'city_id': '131',
        # 'address': '八里庄北里小区',
        'address': '',  # 小区这里 就算是空也得有 address
        'net_type': 'wifi',
        'isp': '',
        'request_time': time.time() * 1000 // 1,
    }

    body_data = {
        'lat': '4828814.459516',
        'lng': '1.296978134979E7',
        'count': '20',  # 每页的数据大小
        'page': '2',  # 第几页
        'bduss': 'NA',
        'stoken': 'bdwm',
        'sortby': '',
        'taste': '',
        'city_id': '131',  # 城市ID
        'promotion': '',
        'return_type': 'paging',
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '133',
        # 'Host': 'client.waimai.baidu.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        # 'Cookie': 'WMST=1520322442; BAIDUID=4924530A6B242C9D17B83A1FD2786386:FG=1; WMID=db6127cd3ab2ae4944a97cbbfec2b1bc',
        'User-Agent': 'okhttp/3.2.0',
    }

    url1 = url.format(urlencode(url_data))

    proxies = {
        "http": "http://10.10.10.81:54321",
        "https": "http://10.10.10.81:54321",
    }

    ss = requests.post(url=url1, data=body_data, headers=headers, proxies=proxies)
    print(ss.status_code)

    print(ss.json())

def get_shop_details():
    url = "http://client.waimai.baidu.com/shopui/na/v1/shopmenu?{}"

    url_data = {
        # 'resid': '1001',
        'from': 'na-android',
        'os': '4.4.4',
        'sv': '3.8.1',
        'cuid': 'F5F020BA348E02E249827BB426C2740E|317570520224668',  # 模拟格式随便填
        'model': 'vivoY13L',
        'screen': '480*854',
        'channel': 'com.xiazaiyewaimai',
        'loc_lat': '4828814.459516',
        'loc_lng': '1.296978134979E7',
        'city_id': '131',
        # 'address': '八里庄北里小区',
        'address': '',  # 小区这里 就算是空也得有 address
        'net_type': 'wifi',
        'isp': '',
        'utm_source': 'waimai',
        'utm_medium': 'shoplist',
        'utm_content': 'default',
        'utm_term': 'default',
        'utm_campaign': 'default',
        'cid': '988272',
        'request_time': time.time() * 1000 // 1,
    }

    body_data = {
        'lat': '4828814.459516',
        'lng': '1.296978134979E7',
        'shop_id': '7946808699115627331',
        'bduss': 'NA',
        'stoken': 'bdwm',
        #'key': 'O%5CFTSTDTT%5CMX%21W3%2F%23%25N%5B%21%26O%5EUPBXV%26O%28VS5.P%273TTRN%11S%5DN%5DPWEXRWEXUQDWSPD%5DQTF%5DTT'
        'key': ''
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '133',
        # 'Host': 'client.waimai.baidu.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        # 'Cookie': 'WMST=1520322442; BAIDUID=4924530A6B242C9D17B83A1FD2786386:FG=1; WMID=db6127cd3ab2ae4944a97cbbfec2b1bc',
        'User-Agent': 'okhttp/3.2.0',
    }

    url1 = url.format(urlencode(url_data))

    proxies = {
        "http": "http://10.10.10.81:54321",
        "https": "http://10.10.10.81:54321",
    }

    ss = requests.post(url=url1, data=body_data, headers=headers, proxies=proxies)
    print(ss.status_code)

    print(ss.json())

def get_shop_comment_list():
    url = "http://client.waimai.baidu.com/mobileui/shop/v1/shopcomment?{}"

    url_data = {
        # 'resid': '1001',
        'from': 'na-android',
        'os': '4.4.4',
        'sv': '3.8.1',
        'cuid': 'F5F020BA348E02E249827BB426C2740E|317570520224668',  # 模拟格式随便填
        'model': 'vivoY13L',
        'screen': '480*854',
        'channel': 'com.xiazaiyewaimai',
        'loc_lat': '4828814.459516',
        'loc_lng': '1.296978134979E7',
        'city_id': '131',
        # 'address': '八里庄北里小区',
        'address': '',  # 小区这里 就算是空也得有 address
        'net_type': 'wifi',
        'isp': '',
        'utm_source': 'waimai',
        'utm_medium': 'shoplist',
        'utm_content': 'default',
        'utm_term': 'default',
        'utm_campaign': 'default',
        'cid': '988272',
        'request_time': time.time() * 1000 // 1,
    }

    body_data = {
        'lat': '4828814.459516',
        'lng': '1.296978134979E7',
        'shop_id': '7946808699115627331',
        'filter_tab': '1',
        'rank': '0',
        'start': '10',  # 开始条数
        'count': '10',  # 每次显示条数
        'bduss': 'NA',
        'stoken': 'bdwm',
        # 'key': 'O%5CFTSTDTT%5CMX%21W3%2F%23%25N%5B%21%26O%5EUPBXV%26O%28VS5.P%273TTRN%11S%5DN%5DPWEXRWEXUQDWSPD%5DQTF%5DTT'
        #'key': ''
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '133',
        # 'Host': 'client.waimai.baidu.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        # 'Cookie': 'WMST=1520322442; BAIDUID=4924530A6B242C9D17B83A1FD2786386:FG=1; WMID=db6127cd3ab2ae4944a97cbbfec2b1bc',
        'User-Agent': 'okhttp/3.2.0',
    }

    url1 = url.format(urlencode(url_data))

    proxies = {
        "http": "http://10.10.10.81:54321",
        "https": "http://10.10.10.81:54321",
    }

    ss = requests.post(url=url1, data=body_data, headers=headers, proxies=proxies)
    print(ss.status_code)

    print(ss.json())



if __name__ == "__main__":

    # 获取店铺列表
    #get_shop_list()

    # 获取店铺详情
    #get_shop_details()

    # 获取店铺评论
    get_shop_comment_list()


