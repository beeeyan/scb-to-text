## 概要


## 初期設定

```conf/const_template.ini
[common]
scb_url = https://scrapbox.io/api/pages/[プロジェクト名]/
cookie = [キー]
```
  
上記ファイルをコピーして`conf/const.ini`ファイルを作成  
(作成したファイルはgitignoreされる)  
以下を変更

「プロジェクト名」 : scrapboxのプロジェクト名
「キー」 : connect.sid

`output`フォルダを作成する。  
(`output`フォルダ自体gitignoreされる)  

## 運用方法

「小説のタイトル + 章番号」でScrapbox上にページを作成する。
  
吾輩は猫である1 みたいな感じ  
  
## 実行方法

```console
$ python main.py タイトル 最大の章番号

$ python main.py 吾輩は猫である 10
```

実行後`./output/' + page_title_base + '_' + now_date + '.txt`の形式でアプトプットされる