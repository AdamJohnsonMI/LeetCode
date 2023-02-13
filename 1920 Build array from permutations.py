class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newList = []
        for i in range(0,len(nums)):
            newList.append(nums[nums[i]])
        return newList    