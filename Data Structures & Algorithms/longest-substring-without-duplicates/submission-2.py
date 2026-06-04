class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen=[]
        max_len=0
        n=len(s)
        for char in s:
            if char in seen:
                #je dois pas supprimer s left mais plutot
                #commencer par le char apres le doublon
                idx=seen.index(char)
                seen=seen[idx+1:]
                

            seen.append(char)
            max_len=max(max_len,len(seen))
            
        return max_len

        