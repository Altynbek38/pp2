def spy_game(nums):
    ok = False
    cnt = 0
    for i in nums:
        if i == 7:
            if(cnt >= 2):
                ok = True
        elif i == 0:
            cnt += 1
    print(ok)






spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 