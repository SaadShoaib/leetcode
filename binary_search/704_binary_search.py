# Solution for binary search
# https://leetcode.com/problems/binary-search/description/

nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    
    left = 0
    right = len(nums) - 1

    while left <= target:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return -1

print(search(nums, target))