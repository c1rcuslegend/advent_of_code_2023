import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        arr = []
        for line in file.readlines():
            a,b=line.split("~")
            arr.append((list(map(int,a.split(","))), list(map(int,b.split(",")))))
        n = len(arr)
        arr.sort(key = lambda x: x[0][2])
        highs=collections.defaultdict(lambda: (0,-1))
        table=set()
        graph, indeg = [[] for _ in range(n)], [0 for _ in range(n)]
        for i,v in enumerate(arr):
            maxx, indexes = -1, set()
            for x in range(v[0][0], v[1][0]+1):
                for y in range(v[0][1], v[1][1]+1):
                    if highs[(x, y)][0] + 1 > maxx:
                        maxx = highs[(x, y)][0] + 1
                        indexes = {highs[(x, y)][1]}
                    elif highs[(x, y)][0] + 1 == maxx:
                        indexes.add(highs[(x, y)][1])
            for x in indexes:
                if x != -1:
                    graph[x].append(i)
                    indeg[i]+=1
            if len(indexes)==1:
                table.add(indexes.pop())
            delta = v[0][2] - maxx
            if delta > 0:
                v[0][2] -= delta
                v[1][2] -= delta
            for x in range(v[0][0], v[1][0] + 1):
                for y in range(v[0][1], v[1][1] + 1):
                    highs[(x, y)] = (v[1][2], i)
        count=0
        for i in range(n):
            cpy, que = indeg[:], collections.deque([i])
            while que:
                u = que.popleft()
                for v in graph[u]:
                    cpy[v]-=1
                    if cpy[v]==0:
                        que.append(v)
                        count+=1
    return count


print(Solution())

