# def count_vowels(s):
#     if len(s) == 0:
#         return "invalid input"
    
#     vowels = "aeiou"
#     distinct_vowels = set()
    
#     for ch in s:
#         if ch in vowels:
#             distinct_vowels.add(ch)
    
#     return len(distinct_vowels)


# print(count_vowels("coole"))


# def pattern(n):
#     for i in range(1,n+1,+1):
#         temp=""
#         for j in range(1,i+1,+1):
#             temp=temp+"*"
#         print(temp)
# pattern(5)

def decreases(x):
    count=0
    for i in range(len(x)-1):
        if x[i-2]>x[i-1]>x[i]:
            count=count+1
    print(count)
decreases([50,48,45,49,47,45,44,41,39])