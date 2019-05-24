import random
your_cash=1000
print("Your Cash = "+str(your_cash))

price=random.randint(100,300)
print("今日のパンの値段は"+str(price)+"です。")
count=1
while your_cash >= price:
    print(str(count)+"回購入")
    your_cash=your_cash - price
    count=count+1
print(str(count)+"回購入しました。")
print("残金は"+str(count)+"円です。")　　　