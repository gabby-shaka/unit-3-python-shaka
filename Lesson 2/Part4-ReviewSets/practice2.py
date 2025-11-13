# 1. 3, 6700
# 2. 0x9F1aB3c...
# 3. 
def portval(holdings, prices):
    total = 0.0
    for coin, amount in holdings.items():
        total += amount * prices[coin]
        return round(total, 2)
