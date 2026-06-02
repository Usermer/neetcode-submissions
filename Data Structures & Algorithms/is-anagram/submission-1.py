class Solution:
    def isAnagram(self,t:str,s:str)->bool:
        return sorted(s)==sorted(t)
       

         