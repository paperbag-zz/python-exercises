# coding: utf-8
def has_33(nums):
    i=0
    ilgis = len(nums)-1
    
    for num in nums:
        if i == ilgis:
            break
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        i+=1
    return False
