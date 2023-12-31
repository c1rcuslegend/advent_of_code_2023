import collections


def Solution():
    PATH = "input.txt"
    order = "AKQJT98765432"
    with open(PATH) as file:
        table, bids = {x: [] for x in [5,7,9,11,13,17,25]}, {}
        for c, b in [_.strip().split() for _ in file.readlines()]:
            bids[c] = int(b)
            table[sum([x ** 2 for x in collections.Counter(c).values()])].append(c)
        ans,count=0,1
        for arr in table.values():
            for s in sorted(arr, key=lambda word: [order.index(char) for char in word],reverse=True):
                ans+=bids[s]*count
                count+=1
    return ans


print(Solution())
