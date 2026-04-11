class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # result=[]
        # for f in nums :
        #     if f not in freq:
        #         freq[f] = 1
        #     else:
        #         freq[f] +=1
        
        # for i in range(k):
        #     result.append(max(freq,key=freq.get))
        #     del freq[max(freq,key=freq.get)]
        
        # return result
        count = Counter(nums)
        heap=[]

        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [num for (freq,num) in heap]
