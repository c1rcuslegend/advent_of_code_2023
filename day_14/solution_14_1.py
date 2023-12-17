from collections import deque
def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        lines=[[x for x in _.strip()] for _ in file.readlines()]
        n,m=len(lines),len(lines[0])
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
        for i,line in enumerate(lines):
            for char in line:
                if char=="O":
                    summ+=n-i

    return summ


print(Solution())

