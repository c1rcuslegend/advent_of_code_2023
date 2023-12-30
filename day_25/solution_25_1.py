import collections
import heapq
import itertools


def Solution():
    PATH = "input.txt"
    with (open(PATH) as file):
        graph = collections.defaultdict(list)
        verts = 0
        for line in file.readlines():
            u,lv=line.strip().split(": ")
            for v in lv.split(" "):
                verts+=1
                graph[u].append(v)
                graph[v].append(u)

        def bfs(start, exeptions={}):
            visited = {start: (0, [start])}
            heap = [(0, start, [start])]
            while len(heap) > 0:
                dist, node, path = heapq.heappop(heap)
                for de in graph[node]:
                    if (node, de) in exeptions:
                        continue
                    if de not in visited:
                        visited[de] = (dist + 1, path + [de])
                        heapq.heappush(heap, (dist + 1, de, path + [de]))
            return (len(visited), visited, node)

        start = next(k for k in graph)
        _, visited, stop = bfs(start)
        for s, d in itertools.pairwise(visited[stop][1]):
            exeptions = {(s, d), (d, s)}
            _, visited2, _ = bfs(start, exeptions)
            for s2, d2 in itertools.pairwise(visited2[stop][1]):
                exeptions = {(s, d), (d, s), (s2, d2), (d2, s2)}
                _, visited3, _ = bfs(start, exeptions)
                for s3, d3 in itertools.pairwise(visited3[stop][1]):
                    exeptions = {(s, d), (d, s), (s2, d2), (d2, s2), (s3, d3), (d3, s3)}
                    lena, _, _ = bfs(start, exeptions)
                    if len(graph) != lena:
                        print((s, d), (s2, d2), (s3, d3))
                        return lena * (len(graph) - lena)


print(Solution())

