import collections
import heapq


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        lines = [[int(c) for c in _.strip()] for _ in file.readlines()]
        n, m = len(lines), len(lines[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, left, up, down
        dist = collections.defaultdict(lambda: float("inf"))
        arr = [(0, 0, 0, -1)]  # summ, i, j, dir
        heapq.heapify(arr)
        vis = set()
        while arr:
            summ, i, j, dir = heapq.heappop(arr)
            if (i, j, dir) in vis:
                continue
            if i == n - 1 and j == m - 1:
                return summ
            vis.add((i, j, dir))
            for k in range(4):
                if k == dir or (k + 2) % 4 == dir:
                    continue
                delta, di, dj = 0, dirs[k][0], dirs[k][1]
                for q in range(1, 11):
                    ii, jj = i + di * q, j + dj * q
                    if 0 <= ii < n and 0 <= jj < m:
                        delta += lines[ii][jj]
                        if q<4 or dist[(ii, jj, dir)] <= delta + summ:
                            continue
                        dist[(ii, jj, dir)] = delta + summ
                        heapq.heappush(arr, (delta + summ, ii, jj, k))
    return


print(Solution())

