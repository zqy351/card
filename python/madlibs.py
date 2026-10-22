# -*- coding: utf-8 -*-
"""
故事填空机 (Python 3.7 兼容)
输入几个词，自动生成一段无厘头爆笑故事。
运行: python3 madlibs.py
"""
import sys


def ask(desc):
    return input("请输入一个{}: ".format(desc)).strip() or "神秘生物"


def build_story(name, adj, animal, place, verb, food, num, exclaim):
    return """
┌─────────────────────────────────────────────┐
  【{}的冒险】· 随机生成的故事

  从前有个叫 {} 的{}勇士，有一天他带着一只{}，
  来到了神秘的{}。突然，{}发出一声巨响！
  {} 激动地大喊：“{}!!!”
  他{}了 {} 口{}，然后心满意足地回家了。
  从此，{}和{}过上了幸福的生活。
└─────────────────────────────────────────────┘
""".format(exclaim, name, adj, animal, place, verb, name, exclaim,
           verb, num, food, name, animal)


def main():
    print("=" * 46)
    print("   📖 故事填空机 —— 你的输入决定剧情")
    print("=" * 46)
    print("（直接回车会使用随机默认词，输入 q 退出）\n")
    name = ask("名字")
    adj = ask("形容词")
    animal = ask("动物")
    place = ask("地点")
    verb = ask("动词")
    food = ask("食物")
    num = ask("数字")
    exclaim = ask("感叹词")
    print(build_story(name, adj, animal, place, verb, food, num, exclaim))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n故事编到一半，下次继续！")
        sys.exit(0)
