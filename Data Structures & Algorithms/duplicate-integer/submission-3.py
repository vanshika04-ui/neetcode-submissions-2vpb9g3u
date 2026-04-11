class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=[] 
        result = False
        for i in range(len(nums)):
            if nums[i] in a:
                result = True
                break
            else:
                a.append(nums[i])
                continue
        return result

                
    