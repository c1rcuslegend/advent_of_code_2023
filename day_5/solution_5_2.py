def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        line = file.readline()
        seed_ranges = [int(_) for _ in line[line.find(":") + 2:].split()]
        seeds, table = [], []
        for j in range(0, len(seed_ranges), 2):
            seeds.append((seed_ranges[j], seed_ranges[j] + seed_ranges[j + 1] - 1))
        file.readline()
        for line in file.readlines():
            line.strip()
            if len(line) == 1:
                seeds += table[:]
                table = []
                continue
            elif not line[0].isnumeric():
                continue
            new, old, step = [int(_) for _ in line.split()]
            new_seeds, d = [], new-old
            for s, e in seeds:
                # match range - {}, our - []
                if s >= old and e <= old + step: # { [] }
                    table.append((s + d, e + d))
                elif s <= old and e >= old + step: # [ {} ]
                    new_seeds.append((s, old - 1))
                    new_seeds.append((old + step - 1, e))
                    table.append((old + d, old + step + d))
                elif old <= s <= old + step <= e: # { [ } ]
                    table.append((s + d, old + step + d))
                    new_seeds.append((old + step + 1, e))
                elif s <= old <= e <= old + step: # [ { ] }
                    table.append((old + d, e + d))
                    new_seeds.append((s, old - 1))
                else: # {} [] or [] {}
                    new_seeds.append((s, e))
                seeds = new_seeds[:]
    return sorted(seeds)[0][0]


print(Solution())

