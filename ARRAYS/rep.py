class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)

        S = n * (n + 1) // 2
        P = n * (n + 1) * (2 * n + 1) // 6

        s = sum(nums)
        p = sum(x * x for x in nums)

        val1 = s - S
        val2 = p - P

        val2 //= val1

        repeat = (val1 + val2) // 2
        missing = repeat - val1

        return [repeat, missing]