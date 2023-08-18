def stock(nums):
    minsofar = nums[0]
    maxprofit = 0

    for i in range(len(nums)):
        minsofar = min(minsofar, nums[i])
        profit = nums[i] - minsofar
        maxprofit = max(maxprofit,profit)
    return maxprofit

print(stock([1,5,3,8,12]))
