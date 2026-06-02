class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dictionnaire=dict()
        # for num in nums:
        #     if num in dictionnaire:
        #         dictionnaire[num]+=1
        #         return True
        #     else:
        #         dictionnaire[num]=1
        # return False
        return len(nums)!=len(set(nums))

       


        
