# -*- coding: utf-8 -*-
"""
超强密码生成器 (Python 3.7 兼容)
生成随机高强度密码：可选手写密码/易读密码/纯数字，
长度 8-64 位，复制即用。
运行: python3 pwd_generator.py
"""
import random
import string
import sys

LOW = string.ascii_lowercase
UP = string.ascii_uppercase
DIG = string.digits
SYM = "!@#$%^&*()-_=+[]{};:,.<>?"


def strong(length, use_sym):
    pool = LOW + UP + DIG + (SYM if use_sym else "")
    # 保证至少包含大小写和数字
    pwd = [random.choice(LOW), random.choice(UP), random.choice(DIG)]
    if use_sym:
        pwd.append(random.choice(SYM))
    while len(pwd) < length:
        pwd.append(random.choice(pool))
    random.shuffle(pwd)
    return "".join(pwd[:length])


def readable(length):
    # 易读版：辅音+元音交替，无易混字符
    cons = "bcdfghjkmnpqrstvwxyz"
    vows = "aeiou"
    pwd = []
    for i in range(length):
        pwd.append(random.choice(cons if i % 2 == 0 else vows))
    return "".join(pwd[:length])


def digits(length):
    return "".join(random.choice(DIG) for _ in range(length))


def main():
    print("=" * 46)
    print("   🔐 超强密码生成器")
    print("=" * 46)
    while True:
        try:
            n = int(input("密码长度 (8-64，回车=16): ").strip() or "16")
        except ValueError:
            print("⚠ 请输入数字")
            continue
        n = max(8, min(64, n))
        print("类型: 1=高强度(含符号) 2=高强度(无符号) 3=易读 4=纯数字")
        t = input("请选择 (回车=1): ").strip() or "1"
        if t == "2":
            p = strong(n, False)
        elif t == "3":
            p = readable(n)
        elif t == "4":
            p = digits(n)
        else:
            p = strong(n, True)
        print("\n🔑 你的密码: {}\n".format(p))
        more = input("再生成一个？(y/n): ").strip().lower()
        if more not in ("y", "yes", "是", ""):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
