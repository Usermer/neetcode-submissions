class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #normallement most_common return the most common and its occurence
        return [element for element,count in Counter(nums).most_common(k)]
    #inside the tuple (3,3)(2,2)