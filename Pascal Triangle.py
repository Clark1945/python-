#Leetcode 帕斯卡三角形 解題
numRows=5
result=[[1]]
for i in range(numRows-1):
    temp=[0]+result[-1]+ [0]
    row=[]
    print(temp)
    for j in range(len(result[-1])+1):
        row.append(temp[j]+temp[j+1])
    result.append(row)
print(result)
