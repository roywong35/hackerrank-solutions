def maximumToys(prices, k):
    sorted_price = sorted(prices)
    count = 0
    for price in sorted_price:
        k -= price
        if k < 0:
            return count
        count += 1
    return count