class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def subset_helper(start, n, nums, current_subset=None, all_subsets=None):
            if all_subsets == None:
                all_subsets = []
            if current_subset == None:
                current_subset = []
            all_subsets.append(current_subset[:])
            for j in range(start, n):
                current_subset.append(nums[j])
                subset_helper(j + 1, n, nums, current_subset, all_subsets)
                current_subset.pop()
            return all_subsets

        return subset_helper(0, len(nums), nums)
