class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result=[]
        for f in nums :
            freq[f] = freq.get(f,0)+1
        
        for i in range(k):
            result.append(max(freq,key=freq.get))
            del freq[max(freq,key=freq.get)]
        
        return result
