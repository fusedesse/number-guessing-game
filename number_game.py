import random

print("数字当てゲーム")

answer = random.randint(100, 999)

attempts = 0
max_attempts = 10

while attempts < max_attempts:

    guess = int(input("100～999の数字を入力してください："))

    attempts += 1

    print("挑戦回数:", attempts)

    print("入力した数字:", guess)

    if guess == answer:
        print("正解")
        break

    elif guess < answer:
        print("もっと大きい数字です")

    else:
        print("もっと小さい数字です")

if attempts == max_attempts and guess != answer:
    print("ゲームオーバー")
    print(f"正解は {answer} でした")