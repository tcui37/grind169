class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def get_val(i, matrix):
            r = i // n
            c = i % n
            return matrix[r][c]

        def binsearch(l, r, matrix, target):
            if l == r:
                return get_val(l, matrix) == target
            m = (r + l) // 2
            print(get_val(m, matrix))
            if get_val(m, matrix) < target:
                return binsearch(m + 1, r, matrix, target)
            else:
                return binsearch(l, m, matrix, target)

        return binsearch(0, m * n - 1, matrix, target)
