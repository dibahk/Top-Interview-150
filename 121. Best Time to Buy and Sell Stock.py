class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy_price = prices[0]
        
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            prof = max(prof, p - buy_price)
        
        return prof
        
