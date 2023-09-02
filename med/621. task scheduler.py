class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f = {}
        l = len(tasks)
        for t in tasks:
            f[t] = f.get(t, 0) + 1

        mf = max(f.values())
        n_mf = 0
        for t in f:
            if f[t] == mf:
                n_mf += 1
        return max(l, (mf - 1) * (n + 1) + n_mf)
