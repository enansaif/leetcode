class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        l, r = 0, n
        t, b = l, r

        k = 1
        while l <= r and t <= b:
            for i in range(l, r):
                grid[t][i] = k
                k += 1
            t += 1
            for i in range(t, b):
                grid[i][r - 1] = k
                k += 1
            r -= 1
            if l > r or t > b:
                break
            for i in range(r - 1, l - 1, - 1):
                grid[b - 1][i] = k
                k += 1
            b -= 1
            for i in range(b - 1, t - 1, - 1):
                grid[i][l] = k
                k += 1
            l += 1
        return grid