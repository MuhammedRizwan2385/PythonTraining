"""Buy and sell stock.
Given a list of ending bell stock prices for n days, compute the maximum profit from buying on a day and selling on any day after the buy operation.
  Example:
Input: [215, 265, 250, 200, 240, 260, 230]
Output: 60"""

stocks=[215,265,250,200,240,260,230]
minSoFar=float('inf')
max_profit=0
for i in stocks:
    minSoFar=min(minSoFar,i)
    max_profit=max(max_profit,i-minSoFar)
print(max_profit)

    

