# def numbers(a,b):
#     for i in range(0,len(a)):
#         if a[i]==b:
#             return "found"
#     return "not found"
# print(numbers([1,2,3,4,5,44,88,90],90))

# def sum(a):
#     sum=0
#     for i in range(0,len(a)):
#         sum=sum+a[i]
#     if sum%2==0:
#         print("even")
#     else:
#         print("odd")
# sum([1,2,3,4,5])


# def check(num_list,a,b):
#     for i in range(0,len(num_list)):
#         if num_list[i]>=a and num_list[i]<=b:
#             print(num_list[i])
# check([8, 1, 0, 19, 11, 28, 3, 5],10,20)

# def fac(x):
#     a=1
#     for i in range(1,x+1):
#         a=a*i
#     print(a)
# fac(5)

# def fact(a):
#     if a==1:
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(5))



# def score(a):
#     p_count=0
#     f_count=0
#     for i in range(0,len(a)):
#         if a[i]>=40:
#             p_count+=1
#         elif a[i]<40:
#             f_count+=1
#     print("Passed",p_count)
#     print("Failed",f_count)
# score([90,40,33,23,28,76])

def product(a):
    count=0
    for i in range(0,len(a),+1):
        if a[i]>1000:
            count=count+1
    return count

print(product([999,818,1002,1004,312]))



