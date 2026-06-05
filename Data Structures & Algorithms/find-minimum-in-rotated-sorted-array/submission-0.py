class Solution:
    def findMin(self, nums: List[int]) -> int:
        #space complexity O(log n)
        #time complexity O(1)
        # n=len(nums)
        # for i in range(1,n):
        #     if nums[i]<nums[0]:
        #         return nums[i]
        # return nums[0]

        #binary search time complexity O(log n)
        n=len(nums)
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2
            if nums[right]<nums[mid]:
                left=mid+1
            else:
                right=mid
        return nums[left]

        