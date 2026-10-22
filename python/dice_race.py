# -*- coding: utf-8 -*-
"""
骰子赛跑 (Python 3.7 兼容)
两个骰子从 0 开始赛跑，先到 50 格获胜。
每轮按回车掷骰，实时显示赛道动画。
运行: python3 dice_race.py
"""
import random
import sys
import time

FINISH = 50


def roll():
    return random.randint(1, 6)


def draw(a, b):
    line_a = ["·"] * FINISH
    line_b = ["·"] * FINISH
    if a < FINISH:
        line_a[a] = "A"
    if b < FINISH:
        line_b[b] = "B"
    print("A |" + "".join(line_a) + "| ({}/{})".format(min(a, FINISH), FINISH))
    print("B |" + "".join(line_b) + "| ({}/{})".format(min(b, FINISH), FINISH))


def main():
    print("🎲 骰子赛跑：A 和 B 掷骰子，先到 {} 格赢！每轮按回车掷骰。".format(FINISH))
    print("（输入 q 退出）")
    a = b = 0
    turn = 0
    while a < FINISH and b < FINISH:
        turn += 1
        r = input("回车掷骰 (第 {} 轮): ".format(turn)).strip().lower()
        if r in ("q", "quit"):
            print("赛跑中止~")
            return
        ra, rb = roll(), roll()
        a += ra
        b += rb
        print("  A 掷出 {}，B 掷出 {}".format(ra, rb))
        draw(a, b)
        time.sleep(0.3)

    if a >= FINISH and b >= FINISH:
        print("🤝 同时到达，平局！")
    elif a >= FINISH:
        print("🏆 A 获胜！")
    else:
        print("🏆 B 获胜！")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
