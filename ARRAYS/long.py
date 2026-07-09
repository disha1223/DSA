class Solution:
    def longestSubarray(self, nums, k):
        left = 0
        curr_sum = 0
        max_len = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == k:
                max_len = max(max_len, right - left + 1)

        return max_len

class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        max_len = 0
        prefix_map = {}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == k:
                max_len = i + 1

            if (prefix_sum - k) in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_len