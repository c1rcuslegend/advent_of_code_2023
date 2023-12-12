def Solution():
    PATH="input.txt"
    summ=0
    with open(PATH) as file:
        strs={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9",
              "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
        for line in file.readlines():
            li,ri=float("inf"),-float("inf")
            l=r=""
            for s,v in strs.items():
                temp=line.find(s)
                if temp!=-1 and temp<li:
                    l,li=v,temp
            for s,v in strs.items():
                temp=line.rfind(s)
                if temp!=-1 and temp>ri:
                    r,ri=v,temp
            summ+=int(l+r)
    return summ

print(Solution())


