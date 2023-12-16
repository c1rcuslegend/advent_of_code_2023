def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        lines = [[x for x in _.strip()] for _ in file.readlines()]
        transposed_lines = list(zip(*lines))
        n, m = len(lines), len(lines[0])
        indexes=[]
        for i in range(n):
            for j in range(m):
                if lines[i][j]=="#":
                    indexes.append((i,j))
        for i in range(len(indexes)):
            x1,y1=indexes[i]
            for j in range(i+1,len(indexes)):
                x2,y2=indexes[j]
                dist=0
                for k in range(min(x1,x2)+1,max(x1,x2)+1):
                    dist+=1 if "#" in lines[k] else 1000000
                for k in range(min(y1,y2)+1,max(y1,y2)+1):
                    dist+=1 if "#" in transposed_lines[k] else 1000000
                summ+=dist
    return summ


print(Solution())

