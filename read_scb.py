import configparser
import requests

# 定数の取得
const = configparser.ConfigParser(interpolation=None)
const.read('conf/const.ini')
scb_url = const.get('common','scb_url')
cookie = const.get('common','cookie')
break_text = '------------'

scb_url = scb_url + '休んだ日には雨が降る1'
cookies={'connect.sid': cookie}

def get_lines_by_page():
    r = requests.get(scb_url, cookies=cookies)
    # 一行目はタイトルなので、タイトル以降
    lines = r.json()['lines'][1:]
    result = ''
    for line in lines:
        if line['text'] == break_text:
            break
        # Scrapboxのリンクはなしにする。
        # print(line['text'].replace('[', '').replace(']', ''))
        result += line['text'].replace('[', '').replace(']', '') + '\n'
    return result
    
    # print(r.json()['lines']);