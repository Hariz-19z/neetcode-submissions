class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)

        my_dict={}

        for i in range(n):
            remainder=target-nums[i]
            if remainder in my_dict:
                return [my_dict[remainder], i]
            my_dict[nums[i]] = i

