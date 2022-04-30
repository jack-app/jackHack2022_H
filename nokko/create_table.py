import sqlite3

def create_table():
    # データベースを作成

    conn = sqlite3.connect('example.db')

    # 前のデータベースを消去し初期化
    conn.execute('DROP TABLE データ')

    # データベースを作成、列IDはデータを追加したとき列番号を自動で付与する
    conn.execute(
    'CREATE TABLE データ(列ID INTEGER PRIMARY KEY AUTOINCREMENT, お題 STRING, 五感 STRING, 回答 STRING, 回答個数 INTEGER)'
    )

    conn.commit()
    conn.close()

def add_table(odai, gokan, kaito):
    # データベースに追加

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    
    # 同じお題・五感・回答の個数を取得
    curkosu = cur.execute('SELECT EXISTS (SELECT * FROM データ WHERE お題=? AND 五感=? AND 回答=?)', [odai, gokan, kaito])
    for row in curkosu:
        kosu = row[0] + 1

    # 追加
    cur.execute('INSERT INTO データ(お題, 五感, 回答, 回答個数) values(?, ?, ?, ?)', [odai, gokan, kaito, kosu])
    curkosu.close()

    conn.commit()
    cur.close()
    conn.close()

def check_table():
    # データベースを確認、確認用のみ

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM データ')

    print(cur.fetchall())

    cur.close()
    conn.close()

# 以下テスト用
#create_table()
#add_table("レモン", "味覚", "酸っぱい")
#add_table("レモン", "味覚", "酸っぱい")
#add_table("レモン", "味覚", "苦い")
#add_table("レモン", "視覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#add_table("バナナ", "味覚", "黄色い")
#check_table()