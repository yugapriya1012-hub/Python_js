# 1
# def first_last(x):
#         print(x[0],x[len(x)-1])
# first_last("yugapriya")

# 2
#count vowels
# def string(a):
#     count=0
#     vowel="aeiouAEIOU"
#     for i in range(len(a)):
#         if a[i] in  vowel:
#             count+=1
#     return count
# print(string("kayal"))

# 3
# count the words
# def count_word(x):
#     count=0
#     a=x.split(" ")
#     for i in a:
#         count+=1
#     return count
# print(count_word("python is fun language"))


# 4
# replace
# def replace_vowels(x):
#     str=""
#     vowels="aeiouAEIOU"
#     for i in range(0,len(x)):
#         if x[i] in  vowels:
#             str=str+"-"
#         else:
#             str=str+x[i]
#     return str
# print(replace_vowels("banana"))
# print(replace_vowels("arrow"))

# 5
# # removed vowels
# def removed_vowels(x):
#     str1=""
#     vowels="aeiouAEIOU"
#     for i in range(len(x)):
#         if x[i] not in  vowels:
#             str1=str1+x[i]
#     return str1
# print(removed_vowels("education"))
# print(removed_vowels("academy"))

# 6
#removed digit in string
# def remove_digit(x):
#     str1=""
#     numbers="1234567890"
#     for i in range(len(x)):
#         if x[i] not in numbers:
#             str1=str1+x[i]
#     return str1
# print(remove_digit( "He12llo"))
# print(remove_digit("Py00th55on"))

# 7
# reverse the word
# # def reverse(x):
# #     rev=""
# #     for i in range(0,len(x)):
# #         rev=x[i]+rev+" "
# #     return rev
# # print(reverse("Abc def"))

# 8
# def count(word,letter):
#     count=0
#     for i in word:
#         if i==letter:
#             count=count+1
#     return count
# print(count("Mississippi","s"))

# 9
#palindrome
# def check(x):
#     rev=""
#     for i in x:
#         rev=i+rev
#     if x==rev:
#         print("yes")
#     else:
#         print("No")
# check("level")
# check("section")

# 10
# Sample Input: [10, 20, 30]
# Expected Output: [-10.0, 0.0, 10.0]

# def avg(a):
#     sum=0
#     count=0
#     b=[]
#     for i in a:
#         sum=sum+i
#         count=count+1
#     average=sum/count
#     for j in a:
#         total=j-average
#         b.append(total)

#     return b
# print(avg([10,20,30]))


# 11
# Square Each Number in a List
# def square(a):
#     b=[]
#     for i in a:
#         c=i**2
#         b.append(c)
#     return b
# print(square([2,3,4,5]))

# 12
# - Count Occurrences of a Given Number
#   Write a program to count how many times a specific number appears in a list.

# def check(a,b):
#     count=0
#     for i in a:
#         if i==b:
#             count=count+1
#     return count
# print(check([3, 5, 3, 8, 3, 9],3))


# 13
# - Replace Negative Numbers with 0
#   Write a program that replaces all negative numbers in a list with 0.


# def replace(a):
#     b=[]
#     for i in a:
#         if i<0:
#             b.append(0)
#         else:
#             b.append(i)
#     return b
# print(replace([5,-3,9,-8,2]))

# 14
# Count Elements Greater Than 50
# def count(a):
#     count=0
#     for i in a:
#         if i>50:
#             count=count+1
#     return count
# print(count([20,60, 75, 45, 90, 35]))


# 15
# Sum of First and Last Elements
# def first_last(x):
#         a=x[0]
#         b=x[len(x)-1]
#         sum=a+b
#         print(sum)
# first_last([10,20,30,40,50])


# 16
#  Write a program to print each element along with its index position.
# def index(a):
#     for i in range(0,len(a)):
#         print("Index",i,a[i])
# index(["apple","banana","grapes"])

# 17
# - Find Sum of Odd and Even Numbers Separately
#   Write a program that finds the sum of all odd numbers and even numbers in a list separately.

# def sum_odd_even(a):
#     odd=0
#     even=0
#     for i in a:
#         if i%2==0:
#             even=even+i
#         else:
#             odd=odd+i
#     print('even_sum =',even ,'odd_sum =',odd)
# sum_odd_even([10,15,20,25,30])

# 18
# Replace All Negative Numbers with Zero
# Write a program to replace every negative number in a list with 0.


# def replace(a):
#     b=[]
#     for i in range(len(a)):
#         if i%2!=0:
#             b.append(0)
#         else:
#             b.append(a[i])
#     return b
# print(replace([10, -5, 20, -10, 30]))

# 19
# def check(main_list,sub_list):
#     for i in range(len(main_list)):
#         if main_list[i]==sub_list[0]:
#             if main_list[i+1]==sub_list[1]:
#                 if main_list[i+2]==sub_list[2]:
#                     return "True"
#     return "False"
# print(check([1, 5, 8, 3, 7, 9, 3, 7, 9, 2],[3,7,9]))

# 20
# def check(s1,s2):
#     for i in range(0,len(s1)):
#         temp=s1[i+1:len(s1)]+s1[0:i+1]
#         if temp==s2:
#             return True
#     return False
# print(check("ABCDE","CDEAB"))
# print(check("ABCDE","ACDEB"))


#give a list of score
# def list(a):
#     count=0
#     for i in a:
#         if i>=40:
#             count=count+1
#     return count
# print(list([45,12,39,55,89,70]))

#Given a list of product prices, count how many items cost more than 1000
# def count(a):
#     count=0
#     for i in a:
#         if i>1000:
#             count=count+1
#     return count
# print(count([2900,800,9000,1200,5300,2300]))


# Given a list of cities, print only the cities whose names have more than 6 letters
# def check(a):
#     b=[]
#     for i in a:
#         if len(i)>=6:
#             b.append(i)
#     print(b)
# check(["jeslin","yugapriya","SnehaN"])

# Delete Last K Array Elements
# def remove(arr,k):
#     b=[]
#     for i in range(0,len(arr)-k):
#         b.append(arr[i])
#     return b
# print(remove([10,20,30,40,50],3))


# Sum of Consecutive Pairs

# def sum_cons(arr):
#     total=0
#     for i in range(len(arr)-1):
#         total+=arr[i]+arr[i+1]
#     return total
# print(sum_cons([1,2,3,4,5]))

# Finding the Count of K 
# def find(arr,k):
#     count=0
#     for i in arr:
#         if i==k:
#             count=count+1
#     return count
# print(find([4, 1, 1, 4, 2, 4, 3, 1, 5],4))

# Finding the Missing Element
# def missing_element(a,b):
#     for i in a:
#         if i not in b:
#             return i
# print(missing_element([10,20,30,40,50],[40,10,20,50]))



# Bonus: Don’t use any inbuilt functions.
# Input:
# "Secret   mission   starts   now"
# Output:
# "Secret mission starts now"

# def name(s):
#     result = ""
#     prev_space = False

#     for ch in s:
#         if ch != " ":
#             result += ch
#             prev_space = False
#         else:
#             if not prev_space:
#                 result += " "
#                 prev_space = True
#     return result
# print(name("Secret         mission   starts   now"))


# def reverse(a):
#     rev=""
#     x=a.split()
#     for i in range(len(x)-1,-1,-1):
#         rev+=x[i]+" "
#     return rev
# print(reverse("iron main is flying"))
# print(reverse("I love python"))


# input -> 132
# output->[1,2,3]


# Given a list of integers, check if a number is present in the list or not. Print “found” else, print “not found”

# def check(a,b):
#     for i in a:
#         if i==b:
#             print("found")
#             break
#     else:
#         print("not found")
# check([1,2,3,4,5,6],6)

# Check if the sum of all numbers in a list is even or not
# def sum(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     if sum%2==0:
#         print("Even")
#     else:
#         print("Not Even")
# sum([1,2,3,4,5])

# Given two numbers a and b and a list of numbers num_list. Print all the elements in num_list between a and b.
# For eg, num_list = [8, 1, 0, 19, 11, 28, 3, 5],  a = 10 and b = 20

# def num(a,b,c):
#     for i in a:
#         if i>b and i<c:
#             print(i)
# num([8, 1, 0, 19, 11, 28, 3, 5],10,20)

#test case 1:
# Input: nums = [4,6,9,2,3,11], k = 2
# Output: [3,11,4,6,9,2]

# def rotate(a,k):
#     result=[]
#     for i in range(k,len(a)):
#         result.append(a[i])
#     for i in range(0,k):
#         result.append(a[i])
#     print(result)
# rotate([10,20,30,40,50],2)

#print index in find value
# def index(a,b):
#     result=[]
#     for i in range(0,len(a)):
#         if b==a[i]:
#             result.append(i)
#     if result:
#         return result
#     else:
#         return "Not found"
# print(index([4,2,7,2,9,3,2,8],2))
# print(index([1,2,3,4,5],6))
        
# Input: nums = [1,3,7,8,9]
# Output: [9,8,7,3,1]

# def rotate(a,k):
#     result=[]
#     for i in range(k,len(a)):
#         result.append(a[i])
#     for i in range(0,k):
#         result.append(a[i])
#     return result
# print(rotate([1,2,3,4,5],3))

#count uppercase
# def count(a):
#     b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     count=0
#     for i in range(0,len(a)):
#         if a[i] in b:
#             count+=1
#     return count
# print(count("HelloWorld"))

# def sentences(a):
#     words=a.split()
#     longest_word=words[0]
#     for i in words:
#         if len(i)>len(longest_word):
#             longest_word=i
#     print(longest_word)
# sentences("Johannesburg is the most populous city of South Africa")

# def swap_around_and(sentence):
#     words = sentence.split()

#     for i in range(1, len(words) - 1):
#         if words[i] == "and":
#             words[i - 1], words[i + 1] = words[i + 1], words[i - 1]

#     return " ".join(words)

# print(swap_around_and("apple and banana"))

# def swap_around_and(sentence):
#     words = sentence.split()

#     for i in range(0, len(words) - 1):
#         if words[i] == "and":
#             words[i - 1], words[i + 1] = words[i + 1], words[i - 1]
#             # print(words)  #['banana', 'and', 'apple', 'the', 'words', 'that', 'appear', 'before', 'and', 'after', 'every', 'occurrence', 'of', 'the', 'word']

#     result = ""
#     for i in range(len(words)):
#         result += words[i]
#         if i != len(words) - 1:
#             result += " "

#     return result

# print(swap_around_and("apple and banana the words that appear before and after every occurrence of the word "))



