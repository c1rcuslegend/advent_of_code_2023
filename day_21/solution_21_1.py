import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        lines=[[x for x in _.strip()] for _ in file.readlines()]
        n, m, que, vis, count = len(lines), len(lines[0]), collections.deque(), set(), 1
        for i in range(n):
            for j in range(m):
                if lines[i][j]=="S":
                    que.append((i,j))
                    vis.add((i,j))
                    break
        time=1
        while que and time!=65:
            for k in range(len(que)):
                i,j=que.popleft()
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ii,jj=i+di,j+dj
                    if 0<=ii<n and 0<=jj<m and lines[ii][jj]!="#" and (ii,jj) not in vis:
                        vis.add((ii,jj))
                        que.append((ii,jj))
                        if time%2==0:
                            count+=1
            time += 1
    return count


print(Solution())


