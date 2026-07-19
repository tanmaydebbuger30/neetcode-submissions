class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for current_price in prices[1:]:
            if current_price < lowest_price:
                lowest_price = current_price
            else: 
                current_profit = current_price - lowest_price
            
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
            

        