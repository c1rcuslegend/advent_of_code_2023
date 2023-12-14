def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        time_l = file.readline()
        dist_l = file.readline()
        time = int("".join(time_l[time_l.index(":") + 2:].strip().split()))
        dist = int("".join(dist_l[dist_l.index(":") + 2:].strip().split()))
        count = 0
        for k in range(time // 2 + 1):
            if k * (time - k) > dist:
                    count = k
                    break
    return (time // 2 + 1 - count) * 2 if time % 2 != 0 else (time // 2 + 1 - count) * 2 - 1


print(Solution())

