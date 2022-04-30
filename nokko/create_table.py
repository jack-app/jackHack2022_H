import sqlite3, numpy as np

def create_table():
    # データベースを作成

    conn = sqlite3.connect('example.db')

    # 前のデータベースを消去し初期化
    conn.execute('DROP TABLE データ')

    # データベースを作成、列IDはデータを追加したとき列番号を自動で付与する
    conn.execute(
    'CREATE TABLE データ(列ID INTEGER PRIMARY KEY AUTOINCREMENT, お題 STRING, 五感 STRING, 回答 STRING, 回答個数 REAL)'
    )

    conn.commit()
    conn.close()

def add_table(odai, gokan, kaito):
    # データベースに追加

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    
    # 同じお題・五感・回答の個数を取得
    curkosu = cur.execute('SELECT COUNT(*) FROM (SELECT * FROM データ WHERE お題=? AND 五感=? AND 回答=?)', [odai, gokan, kaito])
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

def kakuritsu_table(odai, gokan):
    # 答えを返す

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    # お題・五感・回答を回答個数順にソートし、別のデータベースとして作成
    cur.execute('DROP TABLE ソートデータ')
    cur.execute('CREATE TABLE ソートデータ AS SELECT お題, 五感, 回答, MAX(回答個数) AS 回答頻度 FROM データ WHERE お題=? \
    AND 五感=? GROUP BY お題, 五感, 回答', [odai, gokan])
    
    # 確率の分母を出すため、回答個数の合計を出す
    curtotal = cur.execute('SELECT SUM(回答頻度) AS total FROM ソートデータ')
    for row in curtotal:
        bunbo = row[0]

    # 各行の確率を出す
    cur.execute('SELECT お題, 五感, 回答, 回答頻度 / ? AS 回答確率 FROM ソートデータ', [bunbo])
    lists = cur.fetchall()
    answers = []
    probs = []
    for list in lists:
        answers.append(list[2])
        probs.append(list[3])
    return np.random.choice(answers, p = probs)

    cur.close()
    conn.close()

# 以下テスト用
#create_table()
#add_table("レモン", "味覚", "酸っぱい")
#add_table("レモン", "味覚", "酸っぱい")
#add_table("バナナ", "味覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#add_table("バナナ", "視覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#add_table("レモン", "味覚", "苦い")
#add_table("レモン", "視覚", "黄色い")
#add_table("レモン", "視覚", "黄色い")
#print(kakuritsu_table("レモン", "味覚"))