# Input->[95,85,75,12,11]
# Output->[-3,-13,-23,-86,-87]


# def sum(num):
#     if len(num)==0:
#         return "invalid input"
#     else:
#         sum=0
#         result=[]
#         for i in range(len(num)-3,len(num),+1):
#             sum=sum+num[i]
#         for j in range(0,len(num),+1):
#             a=num[j]-sum
#             result.append(a)
#         print(result)
# sum([95,85,75,12,11])


def rearrange(nums):
    if len(nums)==0:
        return "Invalid input"
    else:
        result=[]
        for i in range(0,len(nums),+1):
            result.append(nums[nums[i]])
        return result
print(rearrange([4,0,2,1,3]))



# Input->["abc","adb","abc","aab"]
# output->["verified","abc1","verified"]

#Input->["user","user","user"]
#output->["verified","user1","user2"]