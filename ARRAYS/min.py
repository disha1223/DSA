class Solution:
    def findMin(self, arr):

        low = 0
        high = len(arr) - 1
        ans = float('inf')

        while low <= high:

            if arr[low] <= arr[high]:
                ans = min(ans, arr[low])
                break

            mid = (low + high) // 2

            ans = min(ans, arr[mid])

            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1

        return ans