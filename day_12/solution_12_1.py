def Solution():
    PATH = "input.txt"
    summ=0
    with open(PATH) as file:
        for line in file.readlines():
            s,nums=line.strip().split()
            nums=[int(x) for x in nums.split(",")]
            def back(s_index,curr,arr_index,prev):
                nonlocal s,summ
                if s_index==len(s):
                    if arr_index==len(nums):
                        summ+=1
                    return
                if arr_index<len(nums) and curr>nums[arr_index]:
                    return
                if s[s_index]==".":
                    if curr!=0 and arr_index<len(nums) and curr<nums[arr_index]:
                        return
                    back(s_index+1,0,arr_index,prev+".")
                elif s[s_index]=="#":
                    if arr_index==len(nums) or (curr==0 and prev and prev[-1]=="#"):
                        return
                    curr+=1
                    if arr_index<len(nums) and curr==nums[arr_index]:
                        arr_index+=1
                        curr=0
                    back(s_index+1,curr,arr_index,prev+"#")
                else:
                    prev_index, ii, check, count = arr_index, s_index, False, 0
                    while ii<len(s):
                        if s[ii] in "#?":
                            count+=1
                        else:
                            break
                        ii+=1
                    if arr_index<len(nums) and curr+count>=nums[arr_index]:
                        check=True
                    temp_curr=curr
                    if ( not (curr==0 and prev and prev[-1]=="#") or not prev) and check:
                        curr+=1
                        if arr_index < len(nums) and curr == nums[arr_index]:
                            arr_index += 1
                            curr=0
                        back(s_index + 1, curr, arr_index, prev + "#")
                    if temp_curr==0:
                        back(s_index+1, 0, prev_index, prev+".")
            back(0,0,0,"")

    return summ


print(Solution())

