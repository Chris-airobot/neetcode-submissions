class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(0, len(nums)):
            if nums[i] in indices:
                return [indices[nums[i]],i]
            value = target - nums[i]
            indices[value] = i



        