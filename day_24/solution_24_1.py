def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        arr=[]
        for line in file.readlines():
            a,b=line.strip().split(" @ ")
            a,b=a.split(", "), b.split(", ")
            arr.append((int(a[0]),int(a[1]),int(b[0]),int(b[1])))
        n, ans, MINN, MAXX = len(arr), 0, 200000000000000, 400000000000000
        for i in range(n):
            for j in range(i+1,n):
                x1,y1,dx1,dy1=arr[i]
                x2, y2, dx2, dy2 = arr[j]
                k1, k2 = dy1/dx1, dy2/dx2
                if k1 == k2: # parallel
                    continue
                b1, b2 = y1-k1*x1, y2-k2*x2
                x = (b2-b1)/(k1-k2)
                y = k1*x+b1
                if (x<x1 and dx1>0) or (x>x1 and dx1<0) or (x<x2 and dx2>0) or (x>x2 and dx2<0):
                    continue
                if MINN <= x <= MAXX and MINN <= y <= MAXX:
                    ans+=1
    return ans



print(Solution())

