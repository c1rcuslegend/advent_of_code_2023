def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        lines=[x[x.index(":")+2:].strip() for x in file.readlines()]
        for line in lines:
            arr1,arr2=[_.strip().split() for _ in line.split("|")]
            score=0
            for q in arr2:
                if q in arr1:
                    score=2*score if score!=0 else 1
            summ+=score
    return summ

print(Solution())


