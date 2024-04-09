n, k = map(int, (input().split()))
prices = list(map(int, (input().split())))

min_price = prices[0]
max_profit = 0

if n > k:
    for price in prices[1:k+1]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    for num, price in enumerate(prices[k + 1:], k + 1):
        min_price = min(prices[num - k:num])
        max_profit = max(max_profit, price - min_price)
else:
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

print(max_profit)
