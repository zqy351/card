# -*- coding: utf-8 -*-
"""
文本迷宫生成器 (Python 3.7 兼容)
递归回溯算法生成随机迷宫，字符画打印，支持求解（显示路径）。
运行: python3 maze_gen.py
"""
import random
import sys


def gen(w, h):
    """生成 w×h 迷宫（宽度、高度为奇数）。返回 0=路 1=墙"""
    w = max(5, w | 1)  # 保证奇数
    h = max(5, h | 1)
    maze = [[1] * w for _ in range(h)]

    def carve(x, y):
        maze[y][x] = 0
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < w - 1 and 0 < ny < h - 1 and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0
                carve(nx, ny)

    carve(1, 1)
    maze[1][0] = 0  # 入口
    maze[h - 2][w - 1] = 0  # 出口
    return maze


def solve(maze):
    """BFS 找入口到出口路径，返回路径坐标集合"""
    h, w = len(maze), len(maze[0])
    start, end = (1, 0), (h - 2, w - 1)
    from collections import deque
    q = deque([start])
    prev = {start: None}
    while q:
        cur = q.popleft()
        if cur == end:
            break
        x, y = cur
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == 0 and (nx, ny) not in prev:
                prev[(nx, ny)] = cur
                q.append((nx, ny))
    path = set()
    cur = end
    if cur in prev:
        while cur is not None:
            path.add(cur)
            cur = prev[cur]
    return path


def show(maze, with_path=True):
    path = solve(maze) if with_path else set()
    for y, row in enumerate(maze):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) in path:
                line += "·"
            elif cell == 1:
                line += "█"
            else:
                line += " "
        print(line)


def main():
    try:
        w = int(input("迷宫宽 (5-41，奇数，回车=21): ").strip() or "21")
        h = int(input("迷宫高 (5-21，奇数，回车=13): ").strip() or "13")
    except ValueError:
        print("⚠ 请输入数字")
        return
    maze = gen(w, h)
    print("\n🗺 生成的迷宫（█=墙，空白=路，·=正确路径）：\n")
    show(maze, with_path=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
