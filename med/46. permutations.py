class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def phelp(i, permutations):
            if i == n:
                permutations.append(nums[:])
            else:
                for j in range(i, n):
                    # swappy swap
                    nums[i], nums[j] = nums[j], nums[i]
                    # inductively do the rest
                    phelp(i + 1, permutations)
                    # undo swappy swap
                    nums[i], nums[j] = nums[j], nums[i]
            return permutations

        return phelp(0, [])
