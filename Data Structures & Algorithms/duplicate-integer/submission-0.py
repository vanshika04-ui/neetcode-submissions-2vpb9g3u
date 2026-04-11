class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if nums[i] in nums[i+1:len(nums)]:
                count+=1
                break
        return count>0
         
         