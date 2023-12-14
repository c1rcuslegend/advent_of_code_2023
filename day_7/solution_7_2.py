import collections


def Solution():
    PATH = "input.txt"
    order = "AKQT98765432J"
    with open(PATH) as file:
        table, bids = {x: [] for x in [5,7,9,11,13,17,25]}, {}
        for c, b in [_.strip().split() for _ in file.readlines()]:
            bids[c] = int(b)
            count=collections.Counter(c)
            temp=0
            if "J" in count:
                temp=count["J"]
                del count["J"]
            if not count:
                table[temp**2].append(c)
                continue
            summ,maxx=0,max(count.values())
            for v in count.values():
                if v==maxx:
                    v+=temp
                    maxx=-1
                summ+=v**2
            table[summ].append(c)
        ans,count=0,1
        for arr in table.values():
            for s in sorted(arr, key=lambda word: [order.index(char) for char in word],reverse=True):
                ans+=bids[s]*count
                count+=1
    return ans


print(Solution())

