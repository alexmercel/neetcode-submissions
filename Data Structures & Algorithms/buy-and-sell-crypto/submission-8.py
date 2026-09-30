class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        res=0
        for i in prices:
            if lowest>i:
                lowest=i
            res = max(res,i-lowest)
        return res

        