def buy_sell_stock(nums):
    profit = float('-inf')
    buy = nums[0]
    for i in range (len(nums)):
        buy = min(buy,nums[i])
        profit = max(profit,nums[i]-buy)
    return profit

if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    profit = buy_sell_stock(nums)
    print(profit)