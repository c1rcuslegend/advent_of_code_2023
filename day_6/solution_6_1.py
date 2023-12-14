def Solution():
    PATH = "input.txt"
    mult = 1
    with open(PATH) as file:
        time_l = file.readline()
        dist_l = file.readline()
        time = [int(_) for _ in time_l[time_l.index(":") + 2:].strip().split()]
        dist = [int(_) for _ in dist_l[dist_l.index(":") + 2:].strip().split()]
        for t, d in zip(time, dist):
            count = 0
            for k in range(t // 2 + 1):
                if k * (t - k) > d:
                    count = k
                    break
            mult *= (t // 2 + 1 - count) * 2 if t % 2 != 0 else (t // 2 + 1 - count) * 2 - 1
    return mult


print(Solution())

