import queue


def highestpeak(isWater):
    m, n = len(isWater), len(isWater[0])
    ans = [[0] * n for _ in range(m)]  # n个0的数组
    d = queue.deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                d.append((i, j))
            ans[i][j] = 0 if isWater[i][j] else -1  # 标记水源为0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    h = 1
    while (d):
        size = len(d)
        for _ in range(size):
            x, y = d.popleft()
            for di in dirs:
                nx, ny = x + di[0], y + di[1]
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = h
                    d.append((nx, ny))
        h += 1
    return ans

