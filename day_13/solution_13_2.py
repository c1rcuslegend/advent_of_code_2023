def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        lines=[]
        for line in file.readlines()+[""]:
            line=line.strip()
            if line!="":
                lines.append(line)
                continue
            def check(arr):
                ans,n,m=0,len(arr),len(arr[0])
                for k in range(1,m):
                    check,lengt=0,min(k,m-k)
                    for line in arr:
                        line="".join(line)
                        if (k>m//2 and line[(k-lengt):k]!=line[k:][::-1]) or (k<=m//2 and line[:k]!=line[k:k+lengt][::-1]):
                            check+=1
                            if check>1:
                                break
                    if check==1:
                        ans+=k
                return ans
            summ+=check(lines)+100*check(list(zip(*lines)))
            lines=[]
    return summ


print(Solution())

