class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        diff = []
       
        for i in range(len(prices)-1):
            calc = prices[i+1] - prices[i]
            diff.append(calc)

        print(diff)


        l = 0
        longest= float('-inf')
        add =0
        for r in range(len(diff)):
            add += diff[r]

            while add < 0 and l <= r:
                add -= diff[l]
                l += 1
            longest = max(longest, add)

        return longest if diff else 0
