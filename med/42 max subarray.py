class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running, largest = float("-inf"), float("-inf")
        for num in nums:
            running = max(num, running + num)
            largest = max(largest, running)
        return largest
