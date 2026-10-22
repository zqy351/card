# -*- coding: utf-8 -*-
"""
猜数字游戏 (Python 3.7 兼容)
电脑随机想一个 1-100 的数字，你来猜。
有区间提示、次数统计、最高记录，可无限循环玩。
运行: python3 guess_number.py
"""
import random
import sys

def play():
    print("=" * 40)
    print("     🎯 猜数字游戏")
    print("=" * 40)
    low, high = 1, 100
    target = random.randint(low, high)
    tries = 0
    best = None

    while True:
        try:
            guess = input("请输入 {}-{} 之间的数字: ".format(low, high)).strip()
            if guess in ("q", "quit", "退出"):
                print("下次再来！")
                return False
            n = int(guess)
        except ValueError:
            print("⚠ 请输入数字哦！")
            continue
        if n < low or n > high:
            print("⚠ 数字要在 {} 和 {} 之间！".format(low, high))
            continue

        tries += 1
        if n < target:
            low = n + 1
            print("🔺 小了，往上猜")
        elif n > target:
            high = n - 1
            print("🔻 大了，往下猜")
        else:
            print("🎉 恭喜！答案就是 {}，你用了 {} 次！".format(target, tries))
            if tries <= 7:
                print("⭐ 神级猜手！")
            elif tries <= 12:
                print("👍 不错不错")
            else:
                print("😅 运气有点差，再接再厉")
            return True


def main():
    wins = 0
    while True:
        if play():
            wins += 1
        again = input("再来一局？(y/n): ").strip().lower()
        if again not in ("y", "yes", "是", ""):
            break
    print("共赢了 {} 局，再见！👋".format(wins))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
