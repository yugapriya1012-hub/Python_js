#Input -> 5
#output ->
# *
# **
# ***
# ****
# *****
#option 1
#  def pattern(x):
#     if x<1:
#         print("invalid input")
#     else:
#         for i in range(1,x+1):
#             temp=""
#             for j in range(1,i+1):
#                 temp=temp+"*"
#             print(temp)
# pattern(5)


#option 2
# def pattern(x):
#     if x < 1:
#         print("invalid input")
#     else:
#         for i in range(1, x+1):
#             print("*" * i)

# pattern(5)


def find_second_max(max):
    # if len(max)<2:
    #     return "No second max"
    longest=max[0]
    second=max[0]
    for i in range(0,len(max),+1):
        if max[i]>longest:
            longest=max[i]
    # print(longest)

    for i in range(len(max)):
        if max[i]<longest:
            second=max[i]
    # print(second)

    for i in range(len(max)):
        if max[i]<longest and max[i]>second:
            second=max[i]

    if longest==second:
        return "No second max"
    else:
        return second
print(find_second_max([2,2,4,5,6,7,7]))