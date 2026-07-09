class Solution:
    def frequencySort(self, s):

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = sorted(freq.keys(), key=lambda x: (-freq[x], x))

        return ans