class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window
        n=len(s2)
        k=len(s1)
        s1=sorted(s1)
        window=list(s2[:k])
        left=0
        if sorted(window)==s1:
            return True
        
        for i in range(k,n):
            
            
            window.append(s2[i])
            window.remove(s2[i-k])
            if sorted(window)==s1:
                return True
           
        return False

        