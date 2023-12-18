import collections


def Solution():
    PATH = "input.txt"
    ans=0
    with open(PATH) as file:
        boxes=collections.defaultdict(list)
        def solve(word):
            summ=0
            for char in word:
                summ+=ord(char)
                summ*=17
                summ%=256
            return summ
        for word in file.readline().strip().split(","):
            if "=" in word:
                label,number=word.split("=")
                summ, index=solve(label), None
                for i, (k, v) in enumerate(boxes[summ]):
                    if k == label:
                        index = i
                        break
                if index is None:
                    boxes[summ].append((label,number))
                else:
                    boxes[summ][index]=(label,number)
            else:
                label=word[:-1]
                summ, index=solve(label), None
                for i,(k,v) in enumerate(boxes[summ]):
                    if k==label:
                        index=i
                        break
                if index is not None:
                    boxes[summ].pop(index)
        for i,li in boxes.items():
            for j,lens in enumerate(li):
                ans+=(i+1)*(j+1)*int(lens[1])
    return ans


print(Solution())

