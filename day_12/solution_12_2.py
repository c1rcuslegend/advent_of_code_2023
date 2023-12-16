from functools import cache

def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        for line in file.readlines():
            s,nums=line.strip().split()
            nums=[int(x) for x in nums.split(",")]
            new_s=s
            nums*=5
            for i in range(4):
                s+="?"+new_s
            s+="." # adding to avoid edge cases

            @cache
            def back(s,gr,curr): # s - string left, gr - groups left, curr - current streak of "#"
                # base case
                if not s:
                    return 1 if (not gr and curr==0) else 0

                # if curr streak is larger than a group, or no groups left and the streak is going
                if (gr and curr>gr[0]) or (not gr and curr>0):
                    return 0

                # if no groups left and there is no "#" after
                if not gr:
                    return 1 if "#" not in s else 0

                ans=0
                if s[0] in "?#":
                    ans+=back(s[1:],gr,curr+1)

                if s[0] in "?.":
                    if gr and curr==gr[0]:
                        ans+=back(s[1:],gr[1:],0)
                    elif curr==0:
                        ans+=back(s[1:],gr,0)

                return ans
            summ+=back(s,tuple(nums),0)
    return summ


print(Solution())

