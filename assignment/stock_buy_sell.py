def buy_sell(prices):
    max_profit = 0
    # profits = []

    buy_index = 0
    buy = prices[0]
    sell = 0

    for index, price in enumerate(prices):
        if price < buy:
            buy = price
            buy_index = index

        if price > sell and index > buy_index:
            sell = price
            max_profit = max([max_profit, sell - buy])

    print(max_profit)
    return max_profit


buy_sell([7, 1, 5, 3, 6, 4])
