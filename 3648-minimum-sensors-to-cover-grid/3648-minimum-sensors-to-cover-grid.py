import math

class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        block_size = 2 * k + 1
        rows = math.ceil(n / block_size)
        cols = math.ceil(m / block_size)
        return rows * cols
