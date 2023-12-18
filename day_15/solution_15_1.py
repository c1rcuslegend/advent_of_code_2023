def Solution():
    PATH = "input.txt"
    ans=0
    with open(PATH) as file:
        for word in file.readline().strip().split(","):
            summ=0
            for char in word:
                summ+=ord(char)
                summ*=17
                summ%=256
            ans+=summ
    return ans


print(Solution())

