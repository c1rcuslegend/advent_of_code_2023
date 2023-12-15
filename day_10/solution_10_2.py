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
        dirs_2={
            0:2,1:3,2:0,3:1
        }
        s_enter = []
        def dfs(i,j,vis,curr):
            nonlocal n,m
            for k,(di,dj) in enumerate([(0,1),(-1,0),(0,-1),(1,0)]):
                ii,jj=i+di,j+dj
                if 0<=ii<n and 0<=jj<m and (ii,jj) not in vis and lines[ii][jj] in cons[k]:
                    vis.add((ii,jj))
                    temp=dfs(ii,jj,vis,lines[ii][jj])
                    if temp:
                        if curr=="S":
                            s_enter.append(k)
                        return temp
                    vis.remove((ii,jj))
            for k, (di, dj) in enumerate([(0, 1), (-1, 0), (0, -1), (1, 0)]):
                ii, jj = i + di, j + dj
                if 0<=ii<n and 0<=jj<m and lines[ii][jj]=="S" and k in dirs[curr]:
                    s_enter.append(dirs_2[k])
                    return vis
        check=False
        for i in range(n):
            for j in range(m):
                if lines[i][j]=="S":
                    vis=dfs(i, j, {(i,j)},"S")
                    check=True
                    break
            if check:
                break
        s_enter.sort()
        for k,v in dirs.items():
            if v==s_enter:
                lines[i][j]=k
        ans=0
        for i in range(n):
            for j in range(m):
                if (i,j) in vis:
                    continue
                count,ii,jj=0,i,j
                while ii<n and jj<m:
                    if (ii,jj) in vis and lines[ii][jj]!="L" and lines[ii][jj]!="7":
                        count+=1
                    ii+=1
                    jj+=1
                if count%2!=0:
                    ans+=1
        return ans


print(Solution())

