import collections
import math


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        step=file.readline().strip()
        file.readline()
        graph={}
        que, count, index = collections.deque(), 0, 0
        for line in file.readlines():
            u,v=line.strip().split(" = ")
            l,r=v[1:-1].split(", ")
            if u[-1]=="A":
                que.append(u)
            graph[u]={"L":l,"R":r}
        ans=[]
        while que:
            count+=1
            if index>=len(step):
                index=0
            for i in range(len(que)):
                node=que.popleft()
                if node[-1]=="Z":
                    ans.append(count-1)
                    continue
                que.append(graph[node][step[index]])
            index+=1
    return math.lcm(*ans)


print(Solution())

