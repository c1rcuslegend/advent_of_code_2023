class Workflow:
    def __init__(self, statements):
        self.statements = []
        for i,state in enumerate(statements):
            if i==len(statements)-1:
                name,res,value, num = "True", state, "", 0
            else:
                name,res=state.split(":")
                value, num = name[0], name[2:]
            self.statements.append((name, res, value, int(num)))

def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        table, helper = {}, {"x":0, "m":1, "a":2, "s":3}
        for line in file.readlines():
            line=line.strip()
            if line=="":
                break
            index=line.find("{")
            name,que=line[:index],line[index+1:-1]
            table[name]=Workflow(line[index+1:-1].split(","))

        def calc_range(q, aa, bb):
            for i, (a, b) in enumerate(q):
                if a <= aa <= b or a <= bb <= b:
                    q[i] = (max(a, aa), min(b, bb))
            return q

        def combs(dest, que, names):
            if dest == 'A':
                ans.append((names, que))
                return
            rest_que, last = [_.copy() for _ in que], table[dest].statements[-1]
            for comp, res, char, num in table[dest].statements[:-1]:
                if '<' in comp:
                    a, b = 1, num - 1
                    a_rest, b_rest = num, 4000
                elif '>' in comp:
                    a, b = num + 1, 4000
                    a_rest, b_rest = 1, num
                que[helper[char]] = calc_range(que[helper[char]], a, b)
                rest_que[helper[char]] = calc_range(rest_que[helper[char]], a_rest, b_rest)
                if res != 'R':
                    combs(res, que, names + '->' + res)
                que = [_.copy() for _ in rest_que]
            if last[1] != 'R':
                combs(last[1], rest_que, names + '->' + last[1])
        ans = []
        combs('in', [[(1,4000)] for _ in range(4)], 'in')
        for names, que in ans:
            mult = 1
            for q in que:
                mult *= q[0][1] - q[0][0] + 1
            summ += mult
    return summ


print(Solution())

