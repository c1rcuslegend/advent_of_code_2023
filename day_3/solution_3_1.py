def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        lines=[x.strip() for x in file.readlines()]
        vis=set()
        for j in range(len(lines)):
            check = False
            start = 0
            for i in range(len(lines[j])):
                if lines[j][i]!="." and not lines[j][i].isnumeric():
                    dirs=[(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)]
                    for dj,di in dirs:
                        if 0<=j+dj<len(lines) and 0<=i+di<len(lines[j]) and lines[j+dj][i+di].isnumeric() and (j+dj,i+di) not in vis:
                            l,r,ii="","",i+di
                            vis.add((j+dj,ii))
                            while ii>=0 and lines[j+dj][ii].isnumeric():
                                l=lines[j+dj][ii]+l
                                vis.add((j+dj,ii))
                                ii-=1
                            ii=i+di+1
                            while ii<len(lines[j+dj]) and lines[j+dj][ii].isnumeric():
                                r+=lines[j+dj][ii]
                                vis.add((j + dj, ii))
                                ii+=1
                            summ+=int(l+r)
        return summ

print(Solution())


