def Solution():
    PATH = "input.txt"
    ans=0
    with open(PATH) as file:
        for line in file.readlines():
            arr=[int(_) for _ in line.strip().split()][::-1]
            stk=[arr[-1]]
            while arr!=[0]*len(arr):
                new_arr=[]
                for i in range(1,len(arr)):
                    new_arr.append(arr[i]-arr[i-1])
                stk.append(new_arr[-1])
                arr=new_arr[:]
            ans+=sum(stk)
    return ans

print(Solution())

