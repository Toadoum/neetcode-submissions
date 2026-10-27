class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}

        for i, j in enumerate(nums):
            if target - j in numsmap:
                return [numsmap[target - j], i]
            else:
                numsmap[j] = i