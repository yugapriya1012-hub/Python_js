#question 1

# find vowels and print the count of the vowels
# def finding_vowel(s,c):
#     first = c[0]
#     last = c[1]

#     f,c = 0,0

#     for i in range(0,len(s),+1):
#         if s[i] == first:
#             f = i
#         if s[i] == last:
#             l = i

#     count = 0
#     vowels = "aeiouAEIOU"
#     for j in range(f,l,+1):
#         if s[j] in vowels:
#             count = count +1
#     print(count)

# finding_vowel("abcideouf",["d","f"])
# finding_vowel("aeibcfou",["b","c"])

#question 2
#option 1
# def reverse_even(x):
#     a=[]
#     for i in range(0,len(x),+1):
#         if i%2==0:
#             a.append(x[i])
#     # print(a)
#     b=[]
#     # print(len(a))
#     for j in range(len(a)-1,-1,-1):
        
#         c=a[j]**2
#         b.append(c)
#     print(b)

# reverse_even([1,2,3,4,5,6])

#option 2

# def reverse_even(x):
#     a=[]
#     for i in range(len(x)-1,-1,-1):
#         if i%2==0:
#             a.append(x[i]**2)
#     return a
# print(reverse_even([1,2,3,4,5,6]))


#question 3
#option 1
# def remove_consecutive(nums):
#     if len(nums)==0:
#         return "invalid input"
#     else:
#         left=0
#         right=1
#         while right<len(nums):
#             if nums[left]!=nums[right]:
#                 left+=1
#                 nums[left]=nums[right]
#             right+=1
#         result=[]
#         for i in range(0,left+1,+1):
#             result.append(nums[i])
#         print(result)
# remove_consecutive([1,1,2,2,2,3,1,1])

#option 2
def remove_consecutive(x):
    result=[]
    result.append(x[0])
    for i in range(0,len(x),+1):
        if x[i]!=result[-1]:
            result.append(x[i])
    return result
print(remove_consecutive([1,1,2,2,2,3,1,1]))
