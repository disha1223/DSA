class Solution:#25/06/2026

    def twoSum(self, arr, target):
        seen={}
        n=len(arr)

        for i in range(n):
            complement=target-arr[i]
            if complement in seen:
                return [seen[complement],i]
            seen[arr[i]] = i

        return []
