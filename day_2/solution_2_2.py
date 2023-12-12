def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        for line in file.readlines():
            line=line.strip()
            semicol_id=line.find(":")
            id=line[5:semicol_id]
            line=line[semicol_id+2:]
            count={"blue":0, "red":0, "green":0}
            for s in line.split("; "):
                for i in s.split(", "):
                    v,n=i.split(" ")
                    count[n]=max(count[n],int(v))
            mult=1
            for v in count.values():
                mult*=v
            summ+=mult
    return summ

print(Solution())

