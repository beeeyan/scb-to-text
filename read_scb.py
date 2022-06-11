### coding: UTF-8
import configparser
import requests

# 定数の取得
const = configparser.ConfigParser(interpolation=None)
const.read('conf/const.ini')
scb_url = const.get('common','scb_url')
cookie = const.get('common','cookie')
break_text = '------------'
cookies={'connect.sid': cookie}

def get_lines_by_page(page_title):
    r = requests.get(scb_url + page_title, cookies=cookies)
    # 一行目はタイトルなので、タイトル以降
    lines = r.json()['lines'][1:]
    result = ''
    for line in lines:
        scb_line : str = line['text']
        if scb_line == break_text:
            break
        # Scrapboxのリンクはなしにする。
        result += scb_line.replace('[', '').replace(']', '') + '\n'
    return result
