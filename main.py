### coding: UTF-8
import datetime
import sys
import read_scb

if len(sys.argv) < 3:
    print("引数の数が不正です")
    sys.exit()
else:
    page_title_base = sys.argv[1]
    max_chapter = int(sys.argv[2])

now_date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
txt_path = './output/' + page_title_base + '_' + now_date + '.txt'

with open(txt_path, mode='a') as f:
    # 文字数計測用
    word_count = 0
    for no in range(1, max_chapter + 1):
        page_title = page_title_base + str(no)
        scb_page_text = read_scb.get_lines_by_page(page_title)
        f.write(scb_page_text)
        # 改行と空白を無くした文字数の計測
        word_count += len(scb_page_text.replace('\n', '').replace('　', '').replace(' ', ''))
        if(no != max_chapter):
            f.write('\n*\n\n')
            word_count += 1

print('文字数 : ' + str(word_count))
