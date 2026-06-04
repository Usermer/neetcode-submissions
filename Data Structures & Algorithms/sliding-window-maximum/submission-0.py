class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        left=0
        window=nums[:k]
        solution=[]
        solution=[max(window)]
        for right in range(k,n):
            
            window.append(nums[right])
            window.remove(nums[left])
            left+=1
            solution.append(max(window))
        return solution
            

        