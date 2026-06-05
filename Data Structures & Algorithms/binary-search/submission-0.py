class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #methode normale
        # if target in nums:
        #     return nums.index(target)
        # return -1
        
        #binary search algorithm
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1