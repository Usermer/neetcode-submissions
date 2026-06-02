class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        groups=dict()
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word]=[word]
        return list(groups.values())

        #with defaultdict
        #groups=defaultdict(list)
        #for word in strs:
        #   sorted_world=''.join(sorted(word))
        #   groups[sorted_word].append(word)
        """
        ce que je fais faire c'est de creer un dictionnaire 
        ou les keys sont le nom unique sorted and the values are the list of anagrams presented in the strs

        """
    
            
