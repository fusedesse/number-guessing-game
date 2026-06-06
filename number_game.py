import random

print("数字当てゲーム")

answer = random.randint(100, 999)

attempts = 0

while True:

    guess = int(input("100～999の数字を入力してください："))

    print("入力した数字:", guess)

    if guess == answer:
        print("正解")
        break

    elif guess < answer:
        print("もっと大きい数字です")

    else:
        print("もっと小さい数字です")