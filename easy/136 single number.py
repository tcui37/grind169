class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            s = s ^ num
        return s
