class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=[] 
        result = False
        for i in range(len(nums)):
            if nums[i] in a:
                result = True
            a.append(nums[i])
        return result

                
    