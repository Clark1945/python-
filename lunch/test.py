# strs=["cba","daf","ghi"]

# print(sum(list(col) != sorted(col) for col in zip(*strs)))

# str_count=0
# for i in zip(*strs):
#     if i!="".join(sorted(i)):
#         str_count+=1
# print(str_count)

nums = [1,1]
indx = -1
count = 0
n = len(nums)

# count the number of non-increasing elements
# for i in range(len(nums)-1):
#     if nums[i] >= nums[i+1]:
#         # print("OK")
#         indx = i
#         count += 1

for x in range(len(nums)-1):
    print(x)
    # if nums[x]>nums[x+1]:
    #     print(nums[x])
# for x in range(len(nums)):
#     print(x)