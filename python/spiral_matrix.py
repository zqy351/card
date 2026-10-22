# -*- coding: utf-8 -*-
"""
螺旋矩阵生成器 (Python 3.7 兼容)
生成 N×N 的数字螺旋方阵，并逐圈打印（超治愈的数学图形）。
运行: python3 spiral_matrix.py
"""
import sys


def spiral(n):
    """返回 n×n 螺旋矩阵（从中心向外 / 从外向内皆可，这里从外向内）"""
    mat = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            mat[top][j] = num; num += 1
        top += 1
        for i in range(top, bottom + 1):
            mat[i][right] = num; num += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                mat[bottom][j] = num; num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                mat[i][left] = num; num += 1
            left += 1
    return mat


def show(mat):
    n = len(mat)
    w = len(str(n * n))
    for row in mat:
        print(" ".join(str(x).rjust(w) for x in row))


def main():
    try:
        n = int(input("螺旋矩阵边长 (2-15，回车=5): ").strip() or "5")
    except ValueError:
        print("⚠ 请输入数字")
        return
    n = max(2, min(15, n))
    print("\n🧵 {}×{} 螺旋矩阵：\n".format(n, n))
    show(spiral(n))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
