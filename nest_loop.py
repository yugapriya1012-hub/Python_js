#It print all numbers
# def nested(matrix):
#     for i in range(0,len(matrix),+1):
#         for j in range(0,len(matrix[i]),+1):
#             print(matrix[i][j])
# nested([[1,2,3],[4,5,6],[7,8,9]])


# def binary(a):
#     prod=1
#     b=[]
#     for i in a:
#         prod*=i
#         # print(prod)
#     for j in a:
#         p=prod//j
#         b.append(p)
#     return b
# print(binary([1,2,4,8]))


#If the matrix have zero it replace all element is zero
# def number(a):
#     if len(a)==0:
#         print("Invalid input")
#     else:
#         row=len(a)
#         column=len(a[0])
#         result=[[0]*column]*row
#         print(result)
# number([[1,2,3],[4,5,0],[7,8,9]])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# def matrix(a):
#     rows = len(a)
#     cols = len(a[0])
#     print(cols)

#     # create empty transpose matrix
#     transpose = []
#     for i in range(cols):
#         row = []
#         for j in range(rows):
#             row.append(a[j][i])
#         transpose.append(row)

#     return transpose

# print(matrix([[1, 2,3],[4, 5 ,6]]))
