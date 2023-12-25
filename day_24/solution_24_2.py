from sympy import Symbol
from sympy import solve_poly_system

def Solution():
    PATH = "input.txt"
    with open(PATH) as file:
        arr=[]
        for line in file.readlines():
            a,b=line.strip().split(" @ ")
            a,b=a.split(", "), b.split(", ")
            arr.append((int(a[0]),int(a[1]),int(a[2]),int(b[0]),int(b[1]),int(b[2])))
        x, y, z, dx, dy, dz = Symbol("x"), Symbol("y"), Symbol("z"), Symbol("dx"), Symbol("dy"), Symbol("dz")
        vars = [x, y, z, dx, dy, dz]
        f = []
        for i,v in enumerate(arr[:3]):
            x0, y0, z0, dx0, dy0, dz0 = v
            t = Symbol('t' + str(i))
            vars.append(t)
            fx = x - x0 + t*(dx+dx0)
            fy = y - y0 + t * (dy + dy0)
            fz = z - z0 + t * (dz + dz0)
            f.append(fx), f.append(fy), f.append(fz)
    return sum(solve_poly_system(f, *vars)[0][:3])


print(Solution())

