import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        lines=[[c for c in _.strip()] for _ in file.readlines()]
        n,m=len(lines),len(lines[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        help={
            "\\":  [2, 3, 0, 1],
            "/": [3, 2, 1, 0]
        }
        def count(u,v,dir_s):
            que, vis, check = collections.deque([(u,v,dir_s)]), set(), True
            while que:
                for k in range(len(que)):
                    i,j,dir=que.popleft()
                    ii,jj=i+dirs[dir][0],j+dirs[dir][1]
                    if (i,j,dir) in vis or ii<0 or ii>=n or jj<0 or jj>=m:
                        vis.add((i, j, dir))
                        continue
                    vis.add((i, j, dir))
                    if dir in [0,1] and lines[ii][jj] == "|":
                        que.append((ii, jj, 3))
                        que.append((ii, jj, 2))
                    elif dir in [2,3] and lines[ii][jj]== "-":
                        que.append((ii, jj, 0))
                        que.append((ii, jj, 1))
                    elif lines[ii][jj] in ".-|":
                        que.append((ii, jj, dir))
                    else:
                        que.append((ii,jj,help[lines[ii][jj]][dir]))
            vis.remove((u,v,dir_s))
            count, vis2 = 0, set()
            for i,j,dir in vis:
                if (i,j) not in vis2:
                    count+=1
                vis2.add((i,j))
            return count
        maxx=0
        for i in range(n):
            maxx=max(maxx,count(i,-1,0))
        for i in range(n):
            maxx=max(maxx,count(i,m,1))
        for j in range(m):
            maxx=max(maxx,count(-1,j,2))
        for j in range(m):
            maxx=max(maxx,count(n,j,3))
    return maxx


print(Solution())

