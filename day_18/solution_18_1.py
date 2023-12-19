def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        dirs={"R":(0,1), "L":(0,-1), "U":(-1,0), "D":(1,0)}
        arr_x = arr_y = 0
        curr = (0, 0)
        summ=0
        for line in file.readlines():
            direction, count, color = line.split()
            y,x=dirs[direction]
            count=int(count)
            summ+=count
            next_curr=(curr[0]+x*count, curr[1]+y*count)
            arr_x+=curr[0]*next_curr[1]
            arr_y+=curr[1]*next_curr[0]
            curr=next_curr
    # calculate area with Gauss's area formula and then use Pick's theorem
    return (arr_x-arr_y)//2 + summ//2 + 1


print(Solution())

