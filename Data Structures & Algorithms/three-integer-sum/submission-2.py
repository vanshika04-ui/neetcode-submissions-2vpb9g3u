class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        for i in range(len(nums)):
            for j in range(i,len(nums)-2):
                if nums[i] + nums[j+1] + nums[j+2] ==0:
                    result.append([nums[i],nums[j+1],nums[j+2]])
                else:
                    j+=1
            i= i+1

        return result