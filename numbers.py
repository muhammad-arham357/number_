nums = [3,2,4]

target=6
half_9=9/2


for i in range(len(nums)-1):
    if nums[i] + nums[i+1] == target:
        list_=[i,i+1]
        print(list_)