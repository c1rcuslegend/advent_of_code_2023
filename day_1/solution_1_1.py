def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        for line in file.readlines():
            line=line[:-1]
            f=l=10
            for i in range(len(line)):
                if f==10 and line[i].isnumeric():
                    f=line[i]
                if l==10 and line[-i-1].isnumeric():
                    l=line[-i-1]
                if l!=10 and f!=10:
                    break
            summ+=int(f+l)
    return summ

print(Solution())
         
