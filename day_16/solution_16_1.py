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
        que, vis, check = collections.deque([(0,-1,0)]), set(), True
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
        vis.remove((0,-1,0))
        count=0
        for i,j,dir in vis:
            if lines[i][j]!="#":
                count+=1
            lines[i][j]= "#"
    return count


print(Solution())

