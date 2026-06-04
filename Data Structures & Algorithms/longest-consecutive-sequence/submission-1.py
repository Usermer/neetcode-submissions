class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sliding window
        if len(nums)==0:
            return 0
        left=0
        nums.sort()
        n=len(nums)
        max_cons=1
        current_cons=1
        for right in range(1,n):
            if nums[right]==nums[left]+1 or nums[right]==nums[left]:
                #ici nums[1]=nums[0]+1
                current_cons+=nums[right]-nums[left]
                left+=1
            else:
                max_cons=max(max_cons,current_cons)
                current_cons=1
                left=right
            
                
        return max(max_cons,current_cons)
                        

        