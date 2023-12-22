import collections
import math


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        arr=[_.strip() for _ in file.readlines()]
        def solve(f):
            lines=[]
            for i in range(5):
                for line in arr:
                    lines.append(5*line.replace("S","."))
            lines=[[c for c in _] for _ in lines]
            n, m, que, vis, fin = len(lines), len(lines[0]), collections.deque(), set(), set()
            start_i,start_j=n//2,m//2
            que.append((start_i,start_j,0))
            vis.add((start_i, start_j,0))
            while que:
                i, j, steps = que.popleft()
                if steps==f:
                    fin.add((i,j))
                else:
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ii,jj=i+di,j+dj
                        if 0<=ii<n and 0<=jj<m and lines[ii][jj]!="#" and (ii,jj,steps+1) not in vis:
                            vis.add((ii,jj,steps+1))
                            que.append((ii,jj,steps+1))
            return len(fin)
    steps = 26501365
    delta = steps%131
    # 3916 34870 96644
    a,b,c=solve(delta),solve(delta+len(arr)),solve(delta+len(arr)*2) # 65 + 131 * 1,2,3
    diff1 = b - a
    diff2 = c - b - diff1
    aa = diff2 // 2
    b = diff1 - (3 * aa)
    c = a - aa - b
    n = math.ceil(steps / len(arr))
    # 630661863455116
    return (aa * n ** 2) + (b * n) + c


print(Solution())

