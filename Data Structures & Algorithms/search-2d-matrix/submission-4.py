class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #time complexity O(n²)
        for liste in matrix:
           if target in liste:
            return True
            break
        return False
        
        #binary search time complexity O(nlogn)
        # for liste in matrix:
        #     left,right=0,len(matrix[0])-1
        #     while left<=right:
        #         mid=(left+right)//2
        #         if liste[mid]==target:
        #             return True
        #             break
        #         elif liste[mid]>target:
        #             right=mid-1
        #         else:
        #             left=mid+1
        # return False

        