# -*- coding: utf-8 -*-
"""
奶牛说话 cowsay (Python 3.7 兼容)
经典 ASCII 奶牛，任意输入一句话让它说。
运行: python3 cowsay.py [你的话]   或   运行后输入
"""
import sys


def cowsay(text):
    if not text:
        text = "Moo~ 说点什么吧"
    lines = text.split("\n")
    width = max(len(l) for l in lines)
    border = "+" + "-" * (width + 2) + "+"

    out = [border]
    if len(lines) == 1:
        out.append("| " + lines[0].ljust(width) + " |")
    else:
        for i, l in enumerate(lines):
            if i == 0:
                out.append("/ " + l.ljust(width) + " \\")
            elif i == len(lines) - 1:
                out.append("\\ " + l.ljust(width) + " /")
            else:
                out.append("| " + l.ljust(width) + " |")
    out.append(border)
    out.append("        \\   ^__^")
    out.append("         \\  (oo)\\_______")
    out.append("            (__)\\       )\\/\\")
    out.append("                ||----w |")
    out.append("                ||     ||")
    return "\n".join(out)


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(cowsay(text))
    else:
        print("🖥  奶牛想说就让它说！(输入 q 退出)\n")
        while True:
            t = input("你说: ").strip()
            if t.lower() in ("q", "quit"):
                break
            print()
            print(cowsay(t))
            print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
