class Workflow:
    def __init__(self, statements):
        self.statements = []
        for i,state in enumerate(statements):
            if i==len(statements)-1:
                name,res,value="True",state,""
            else:
                name,res=state.split(":")
                value=name[0]
            self.statements.append((name, res,value))

def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        table, check, helper = {}, False, {0:"x", 1:"m", 2:"a", 3:"s"}
        for line in file.readlines():
            line=line.strip()
            if check:
                vals={}
                for i,s in enumerate(line[1:-1].split(",")):
                    vals[helper[i]]=int(s[2:])
                name, cycle = "in", True
                while 1:
                    for comp,dest,val in table[name].statements:
                        if comp=="True" or eval(comp,{val:vals[val]}):
                            name=dest
                            break
                    if name == "A":
                        summ += sum(vals.values())
                        break
                    elif name == "R":
                        break
                continue
            elif line=="":
                check=True
                continue
            index=line.find("{")
            name,que=line[:index],line[index+1:-1]
            table[name]=Workflow(line[index+1:-1].split(","))
    return summ


print(Solution())

