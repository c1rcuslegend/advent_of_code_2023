import collections
import math


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        graph, conjucts, flops = {}, {}, {}

        for line in file.readlines():
            name,dest=line.strip().split(" -> ")
            if not name[0].isalpha():
                type = name[0]
                name=name[1:]
            else:
                type = "broad"
            if type=="&":
                conjucts[name]={}
            elif type=="%":
                flops[name]=False
            graph[name]=(type,dest.split(", "))

        for name, (type, li) in graph.items():
            for l in li:
                if l in graph and graph[l][0] == "&":
                    conjucts[l][name] = False

        def dfs(u, d, vis, path):
            vis.add(u)
            path.append(u)
            if u == d:
                g_vis.add(path[-3])
            else:
                for i in graph[u][1]:
                    if i not in vis:
                        dfs(i, d, vis, path)
            path.pop()
            vis.remove(u)

        ans, g_vis, count_2, que = [], set(), 0, collections.deque()
        dfs("broadcaster", "rx", set(), [])

        while len(ans)!=len(g_vis):
            for v in graph["broadcaster"][1]:
                que.append((False,v,"broadcaster"))
            count_2+=1
            while que:
                for i in range(len(que)):
                    signal, dest, fromm = que.popleft()
                    if dest in g_vis and not signal:
                        ans.append(count_2)
                    if dest not in graph:
                        continue
                    type, arr = graph[dest]
                    if type=="broad":
                        out = signal
                    elif type=="%":
                        if signal:
                            continue
                        else:
                            flops[dest]=not flops[dest]
                            out = flops[dest]
                    else:
                        conjucts[dest][fromm], out = signal, False
                        for v in conjucts[dest].values():
                            if not v:
                                out=True
                                break
                    for g in arr:
                        que.append((out,g,dest))
    return math.lcm(*ans)


print(Solution())

