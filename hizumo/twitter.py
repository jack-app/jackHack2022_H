thm="あなたのお題は"
sen="あなたの五感は"
ans="あなたの回答は"
per="あなたの一致度は"
web="https://fivesenseh.herokuapp.com/"
has="#特徴一致ゲーム"

#"１"のところに結果を入れる
def twitter():
    sent=thm+"1"+"。"+sen+"1"+"。"+ans+"1"+"。"+per+"1"+"でした！"+web+has
    print(sent)
    return sent

twitter()





    

