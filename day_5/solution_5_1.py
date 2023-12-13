def Solution():
    PATH="input.txt"
    with open(PATH) as file:
        line=file.readline()
        seeds=[int(_) for _ in line[line.find(":")+2:].split()]
        table={}
        file.readline()
        for line in file.readlines():
            line.strip()
            if len(line)==1:
                for j in range(len(seeds)):
                    seeds[j]=table[seeds[j]] if seeds[j] in table else seeds[j]
                table.clear()
                continue
            elif not line[0].isnumeric():
                continue
            new, old, step = [int(_) for _ in line.split()]
            for seed in seeds:
                if old<=seed<old+step:
                    table[seed]=new+seed-old
    for j in range(len(seeds)):
        seeds[j] = table[seeds[j]] if seeds[j] in table else seeds[j]
    return min(seeds)

print(Solution())


