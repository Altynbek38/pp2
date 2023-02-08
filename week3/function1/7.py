def has_33(nums):
    ok = False
    for i in range(len(nums)):
        if(i == len(nums) - 1):
            break
        if nums[i] == 3 and nums[i + 1] == 3:
            ok = True
    print(ok)


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])