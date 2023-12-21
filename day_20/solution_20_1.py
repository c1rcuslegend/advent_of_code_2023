import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        graph={}
        conjucts={}
        flops={}
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
        que = collections.deque()
        count = {True: 0, False: 0}
        for i in range(1000):
            for v in graph["broadcaster"][1]:
                que.append((False,v,"broadcaster"))
            count[False]+=1
            while que:
                for i in range(len(que)):
                    signal, dest, fromm = que.popleft()
                    count[signal]+=1
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
    return count[False]*count[True]


print(Solution())

