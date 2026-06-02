class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution=[]
        for i in range(len(nums)):
            product=math.prod([nums[j] for j in range(len(nums)) if i != j])
            solution.append(product)
        return solution
       
        # for num in nums:
        #     solution.append(math.prod(nums.remove(num)))
        """
        remove is a function that modify the list in place
        """
        # for num in nums:
        #     nums.remove(num)
        #     solution.append(math.prod(nums))
        #     nums.append(num)
        # return solution
        """
        this method is incorrect because the element is appended is the end of the list
        so the order change
        """
         # for num in nums:
        #     product=math.prod([execeptnum for execeptnum in nums if execeptnum != num])
        #     solution.append(product)
        # return solution

        """
        almost there but When there are duplicate
        numbers in the list, if execeptnum != num removes ALL 
        occurrences of that value, not just the current one. so we should work with indexes
        """