# def right_rotate_sum(a, k):
#     result = ""
#     n = 0

#     # find length manually
#     for ch in a:
#         n += 1

#     # add last k characters first
#     i = n - k
#     while i < n:
#         result = result + a[i]
#         i += 1

#     # add full original string
#     i = 0
#     while i < n:
#         result = result + a[i]
#         i += 1

#     return result


# a = "helloworld"
# k = 2
# print(right_rotate_sum(a, k))
