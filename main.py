import read_scb
import sys

if len(sys.argv) < 3:
    print("引数の数が不正です")
    sys.exit()
else:
    page_title_base = sys.argv[1]
    max_chapter = int(sys.argv[2])

for no in range(1, max_chapter + 1):
    page_title = page_title_base + str(no)
    print(read_scb.get_lines_by_page(page_title))
