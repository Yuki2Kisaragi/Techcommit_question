import random
money_held=1000
print("Money_held = "+str(money_held))   #your_cash->money_held

price=random.randint(100,300)
print("今日のパンの値段は"+str(price)+"です。")
count=0
while True:
    if money_held < price:
        count=count+1
        print(str(count)+"回購入")
        print("")
        money_held=money_held - price
    else:
        break
print(str(count)+"回購入しました。")
print("残金は"+str(money_held)+"円です。")   #count->money_held