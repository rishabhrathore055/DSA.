def stock(nums):
    minsofar = nums[0] # Storing the  first element of the array
    maxprofit = 0

    for i in range(len(nums)):
        minsofar = min(minsofar, nums[i]) # Calulate the min value
        profit = nums[i] - minsofar
        maxprofit = max(maxprofit,profit)
    return maxprofit

print(stock([1,5,3,8,12]))
