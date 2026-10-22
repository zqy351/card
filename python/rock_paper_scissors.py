# -*- coding: utf-8 -*-
"""
石头剪刀布·人机对战 (Python 3.7 兼容)
无限局对战，记录胜负平局与胜率，电脑随机出拳。
运行: python3 rock_paper_scissors.py
"""
import random
import sys

MAP = {"r": "🪨 石头", "s": "✂️ 剪刀", "p": "📄 布"}


def judge(me, ai):
    if me == ai:
        return 0
    if (me, ai) in (("r", "s"), ("s", "p"), ("p", "r")):
        return 1
    return -1


def main():
    wins = loses = draws = 0
    print("🪨✂️📄  石头剪刀布！（输入 r=石头 s=剪刀 p=布，q=退出）")
    while True:
        me = input("\n你出: ").strip().lower()
        if me in ("q", "quit"):
            break
        if me not in MAP:
            print("⚠ 只能输 r / s / p")
            continue
        ai = random.choice(list(MAP.keys()))
        print("你出 {}，电脑出 {}".format(MAP[me], MAP[ai]))
        res = judge(me, ai)
        if res == 1:
            wins += 1
            print("🎉 你赢了！")
        elif res == -1:
            loses += 1
            print("😢 你输了")
        else:
            draws += 1
            print("🤝 平局")
        total = wins + loses + draws
        rate = 100.0 * wins / total if total else 0
        print("📊 战绩：胜 {} / 负 {} / 平 {}，胜率 {:.1f}%".format(wins, loses, draws, rate))

    print("\n最终战绩：胜 {} / 负 {} / 平 {}，感谢游玩！".format(wins, loses, draws))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
