class Solution:
    def findKRotation(self, nums):

        low = 0
        high = len(nums) - 1

        ans = float('inf')
        index = -1

        while low <= high:

            if nums[low] <= nums[high]:
                if nums[low] < ans:
                    ans = nums[low]
                    index = low
                break

            mid = (low + high) // 2

            if nums[mid] < ans:
                ans = nums[mid]
                index = mid

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return index