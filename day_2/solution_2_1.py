def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        for line in file.readlines():
            check=True
            line=line.strip()
            semicol_id=line.find(":")
            id=line[5:semicol_id]
            line=line[semicol_id+2:]
            for s in line.split("; "):
                count={"blue":14, "red":12, "green":13}
                for i in s.split(", "):
                    v,n=i.split(" ")
                    if count[n]<int(v):
                        check=False
                        break
                if not check:
                    break
            if check:
                summ+=int(id)
    return summ

print(Solution())



