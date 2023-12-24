import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        lines=[[c for c in _.strip()] for _ in file.readlines()]
        n, m = len(lines), len(lines[0])
        arr=[(0,1),(n-1,m-2)]
        for i in range(n):
            for j in range(n):
                if lines[i][j]=="#":
                    continue
                count=0
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i+di < n and 0 <= j+dj < m and lines[i+di][j+dj] != "#":
                        count+=1
                if count>2:
                    arr.append((i,j))
        graph = collections.defaultdict(dict)
        for i,j in arr:
            stk, table = collections.deque([(0,i,j)]), {(i,j)}
            while stk:
                k, r, c = stk.popleft()
                if k!=0 and (r,c) in arr:
                    graph[(i,j)][(r,c)] = k
                    continue
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    rr,cc=r+dr,c+dc
                    if 0 <= rr < n and 0 <= cc < m and lines[rr][cc] != "#" and (rr, cc) not in table:
                        table.add((rr,cc))
                        stk.append((k+1,rr,cc))
        vis = [[False for j in range(m)] for i in range(n)]
        def dfs(i,j):
            if (i,j)==(n-1,m-2):
                return 0
            vis[i][j], ans = True, -1
            for ii,jj in graph[(i,j)]:
                if not vis[ii][jj]:
                    ans = max(ans, graph[(i,j)][(ii,jj)] + dfs(ii,jj))
            vis[i][j]=False
            return ans
    return dfs(0,1)


print(Solution())

