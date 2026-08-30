class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        seen = {}

        for i in range(n):
            remainder = target - nums[i]

            if remainder in seen:
                return [seen[remainder], i]

            seen[nums[i]] = i

        return []
        