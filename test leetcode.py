candies=[2,3,5,1,3]
extraCandies = 3
M=max(candies)
for x in range(len(candies)):
    print(candies[x])
    candies[x]= candies[x]+extraCandies>=M
print(candies)