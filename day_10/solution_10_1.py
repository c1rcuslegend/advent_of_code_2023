import sys


def Solution():
    sys.setrecursionlimit(50000)
    PATH = "input.txt"
    with open(PATH) as file:
        lines=[[char for char in s.strip()] for s in file.readlines()]
        n,m=len(lines),len(lines[0])
        cons=["-J7","|F7","-LF","|JL"] # right, up, left, down
        dirs={
            "-":[0,2], "|":[1,3], "L":[0,1], "J":[1,2], "7":[2,3], "F":[0,3]
        }
        def dfs(i,j,vis,curr):
            nonlocal n,m
            for k,(di,dj) in enumerate([(0,1),(-1,0),(0,-1),(1,0)]):
                ii,jj=i+di,j+dj
                if 0<=ii<n and 0<=jj<m and (ii,jj) not in vis and lines[ii][jj] in cons[k]:
                    vis.add((ii,jj))
                    temp=dfs(ii,jj,vis,lines[ii][jj])
                    if temp:
                        return temp
                    vis.remove((ii,jj))
            for k, (di, dj) in enumerate([(0, 1), (-1, 0), (0, -1), (1, 0)]):
                ii, jj = i + di, j + dj
                if 0<=ii<n and 0<=jj<m and lines[ii][jj]=="S" and k in dirs[curr]:
                    return len(vis)
        for i in range(n):
            for j in range(m):
                if lines[i][j]=="S":
                    return dfs(i, j, {(i,j)},"S")//2


print(Solution())


