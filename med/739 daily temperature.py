class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, j = stack.pop()
                days[j] = i - j
            if not stack or temp <= stack[0][0]:
                stack.append((temp, i))
        return days
