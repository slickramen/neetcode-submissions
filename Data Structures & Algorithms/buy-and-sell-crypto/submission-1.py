class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for l in range(len(prices)):
            min_p = prices[l]
            for j in range(l, len(prices)):
                cur_p = prices[j]

                projected_p = cur_p - min_p

                profit = max(projected_p, profit)

        return profit
