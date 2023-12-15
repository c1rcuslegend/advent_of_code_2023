import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        step=file.readline().strip()
        file.readline()
        graph={}
        for line in file.readlines():
            u,v=line.strip().split(" = ")
            l,r=v[1:-1].split(", ")
            graph[u]={"L":l,"R":r}
        que,count=collections.deque([("AAA",0)]),0
        while que:
            node,index=que.popleft()
            if node=="ZZZ":
                return count
            count += 1
            if index>=len(step):
                que.append((graph[node][step[0]],1))
                continue
            que.append((graph[node][step[index]],index+1))
    return -1


print(Solution())

