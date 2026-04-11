class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        i=0
        while i< len(nums):
            j = 0
            res=1
            for j in range(len(nums)):
                if j==i:
                    pass
                else:
                    res = res* nums[j]
                j+=1
            output.append(res)
            i+=1
        return output