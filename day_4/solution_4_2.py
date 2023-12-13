def Solution():
    PATH="input.txt"
    cards={x:1 for x in range(1,221)}
    with open(PATH) as file:
        lines=[x[x.index(":")+2:].strip() for x in file.readlines()]
        for i,line in enumerate(lines):
            arr1,arr2=[_.strip().split() for _ in line.split("|")]
            score=0
            for q in arr2:
                if q in arr1:
                    score+=1
            for j in range(i+2,i+2+score):
                cards[j]+=cards[i+1]
    return sum(cards.values())

print(Solution())


