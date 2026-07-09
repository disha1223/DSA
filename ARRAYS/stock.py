class Solution:
    def stockBuySell(self, arr, n):
        mini = arr[0]
        maxProfit = 0

        for i in range(1, n):
            cost = arr[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, arr[i])

        return maxProfit