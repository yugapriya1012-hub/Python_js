# Implement an algorithm to determine if a string has all unique characters.

# Sample Test Cases:

# "abc" -> True"abba" -> False"" -> False"v" -> True (since it is made up of only one letter)


# def not_repeat(x):
#     if len(x) == 0:
#         return False
    
#     for i in range(0,len(x)):
#         for j in range(i + 1, len(x)):
#             if x[i] == x[j]:
#                 return False
#     return True
# print(not_repeat("c")) #True
# print(not_repeat("aabbc"))  #False



# Write a Python Program to make chunks of the size k and an input list of numbers.

# Input:
# nums = [1,2,3,4,5,6,7,8,9] , k = 4
# Output:  [ [1,2,3,4] , [5,6,7,8], [9] ]

# Test Case 2:
# nums = [1,2,3,4,5,6,7,8,9], k = 3
# Output: [[1,2,3], [4,5,6] , [7,8,9] ]

# def make_chunks(nums, k):
#     result = []
#     temp = []
    
#     for i in range(len(nums)):
#         temp.append(nums[i])
#     # print(temp)
        
#         if len(temp) == k:
#             result.append(temp)
#             temp = []
   
    
#     # # add remaining elements
#     if len(temp) > 0:
#         result.append(temp)
    
#     return result
# print(make_chunks([1,2,3,4,5,6,7,8,9,0],4))


# Implement binary search algorithm

# Sample Test Case 1:
# nums = [15, 24, 30, 48, 49, 64, 86, 90, 100, 121, 130]
# key = 121

# Output: 9  (which means 121 exists at the 9th index)

# Sample Test Case 2:
# Implement binary search algorithm
# nums = [15, 24, 30, 48, 49, 64, 86, 90, 100, 121, 130]
# key = 94

# Output: -1 (which means the number 94 does not exists)


# def name(x,y):
#     if len(x)==0:
#         print("Invalid input")
#     else:
#         for i in range(0,len(x)):
#             if x[i]==y:
#                 return i
#         else:
#             return -1
# print(name([15, 24, 30, 48, 49, 64, 86, 90, 100, 121, 130],121))
# print(name([15, 24, 30, 48, 49, 64, 86, 90, 100, 121, 130],94))



