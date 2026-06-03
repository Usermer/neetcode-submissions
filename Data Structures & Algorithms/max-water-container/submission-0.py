class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = [1,7,2,5,4,7,3,6]
        no storting
        we should multily each number with the distance 
        and declare a max

        """

        n=len(heights)
        left,right=0,n-1
        maximum=0
        while left<right:
            surface=min(heights[left],heights[right])*(right-left)
            maximum=max(maximum,surface)
            #i should add a condition
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maximum

        