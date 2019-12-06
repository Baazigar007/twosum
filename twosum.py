def twosum(nums,target):
    d={}
    for i in range(len(nums)):
        print ("i=",i)
        if nums[i] in d:
            print ("np")
            print ([d[nums[i]],i])
        else:
            print ("d=",d,"target-nums[i]",target-nums[i],"nums[i]",nums[i])
            d[target-nums[i]]=i
    
