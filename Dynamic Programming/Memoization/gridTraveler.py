def gridTraveler(m,n,memo = {}):
    # are the agrs in the memo
    key = str(m) + "," + str(n)
    if (key in memo) : return memo[key]
    if(m==1 and n==1): return 1
    if(m==0 or n==0): return 0
    memo[key] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo)
    return memo[key]

print(gridTraveler(3,3))
print(gridTraveler(3,2))
print(gridTraveler(6,3))
print(gridTraveler(23,18))