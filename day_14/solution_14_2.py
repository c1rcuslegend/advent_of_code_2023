from collections import deque
def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        lines=[[x for x in _.strip()] for _ in file.readlines()]
        n,m=len(lines),len(lines[0])
        vis={}
        def north():
            for j in range(m):
                dots=deque([])
                for i in range(n):
                    if lines[i][j]==".":
                        dots.append(i)
                    elif lines[i][j]=="#":
                        dots.clear()
                    elif dots:
                        pos=dots.popleft()
                        lines[pos][j], lines[i][j] = lines[i][j], lines[pos][j]
                        dots.append(i)
        def west():
            for i in range(n):
                dots=deque([])
                for j in range(m):
                    if lines[i][j]==".":
                        dots.append(j)
                    elif lines[i][j]=="#":
                        dots.clear()
                    elif dots:
                        pos=dots.popleft()
                        lines[i][pos], lines[i][j] = lines[i][j], lines[i][pos]
                        dots.append(j)
        def south():
            for j in range(m):
                dots=deque([])
                for i in range(n-1,-1,-1):
                    if lines[i][j]==".":
                        dots.append(i)
                    elif lines[i][j]=="#":
                        dots.clear()
                    elif dots:
                        pos=dots.popleft()
                        lines[pos][j], lines[i][j] = lines[i][j], lines[pos][j]
                        dots.append(i)
        def east():
            for i in range(n):
                dots=deque([])
                for j in range(m-1,-1,-1):
                    if lines[i][j]==".":
                        dots.append(j)
                    elif lines[i][j]=="#":
                        dots.clear()
                    elif dots:
                        pos=dots.popleft()
                        lines[i][pos], lines[i][j] = lines[i][j], lines[i][pos]
                        dots.append(j)
        k=0
        while k < 1000000000:
            k+=1
            north(), west(), south(), east()
            grid=tuple(zip(*lines))
            if  grid in vis:
                cycle = k - vis[grid]
                temp=(1000000000 - k) // cycle
                k += temp * cycle
            vis[grid] = k
        for i,line in enumerate(lines):
            for char in line:
                if char=="O":
                    summ+=n-i
    return summ


print(Solution())

