# def unique(x):
#     uni={}
#     for i in range(len(x)):
#         if x[i] in uni:
#             uni[x[i]]=uni[x[i]]+1
#         else:
#             uni[x[i]]=1
#     uniq=[]
#     for key in uni:
#         if uni[key]==1:
#             uniq.append(key)
#     return uniq
        
# print(unique([1,2,3,4,1,3,4]))

# split the word without using split
# def split(x):
#     word=[]
#     temp=""
#     for i in range(0,len(x),+1):
#         if x[i]!=" ":
#             temp=temp+x[i]
#         else:
#             word.append(temp)
#             temp=""
#     word.append(temp)
#     return word
            
# print(split("hello everyone"))


#prime number
# def prime(n:int)->bool:
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# print(prime(3))

#split the digit(eg.365),output->[3,6,5]
# def split(x):
#     result=[]
#     if x==0:
#         result.append(0)
#     else:
#         while x>0:
#             digit=x%10
#             result.append(digit)
#             x=x//10
#         result.reverse()
#         return result
# print(split(365))

#Palindrome
# def palindrome(x):
#     if len(x)==0:
#         return False
#     else:
#         l=len(x)
#         for i in range(0,l,+1):
#             if x[i]!=x[l-i-1]:
#                 return False
#         return True
# print(palindrome("level"))
# print(palindrome("search"))


#input->IceCream,output->aceCreIm
# def vowels(x:str)->str:
#     vowel_char=[]
#     indices=[]
#     vowels="aeiouAEIOU"

#     for i in range(len(x)):
#         if x[i] in vowels:
#             indices.append(i)
#             vowel_char.append(x[i])

#     word=list(x)
#     l=len(indices)

#     for j in range(l):
#         idx=(indices[j])
#         letter=(vowel_char[l-j-1])
#         word[idx]=letter
#     return "".join(word)
# print(vowels("IceCream"))


