import collections


def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        lines=[[c for c in _.strip()] for _ in file.readlines()]
        que=collections.deque([(0, 1, {(0, 1)})])
        dirs = {">":(0,1, 2), "<":(0,-1, 3), "^":(-1,0, 1), "v":(1,0, 0)}
        help = ["#^","#v","#<","#>"]
        n, m =  len(lines), len(lines[0])
        maxx = 0
        while que:
            i, j, vis = que.popleft()
            if i==n-1 and j==m-2:
                maxx=max(len(vis)-1, maxx)
                continue
            if lines[i][j] in dirs:
                di, dj, dir = dirs[lines[i][j]]
                if 0<=i+di<n and 0<=j+dj<m and lines[i+di][j+dj] not in help[dir] and (i+di, j+dj) not in vis:
                    vis.add((i+di, j+dj))
                    que.append((i+di, j+dj, vis))
                    continue
            for dir,(di,dj) in enumerate([(1,0),(-1,0),(0,1),(0,-1)]): # down, up, right, left
                ii,jj=i+di,j+dj
                if 0<=ii<n and 0<=jj<m and lines[ii][jj] not in help[dir] and (ii, jj) not in vis:
                    temp=vis.copy()
                    temp.add((ii, jj))
                    que.append((ii, jj, temp))
    return maxx


print(Solution())

