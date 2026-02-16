# # xo game
# #option 1
# def check_winner(board):
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2] and row[0] != "O" and row[0] != "X":
#             pass
#         if row[0] == row[1] == row[2]:
#             return f"{row[0]} winner"

#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col]:
#             return f"{board[0][col]} winner"

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2]:
#         return f"{board[0][0]} winner"

#     if board[0][2] == board[1][1] == board[2][0]:
#         return f"{board[0][2]} winner"

#     return "Draw"


# # Input
# board = [
#     ["O", "O", "X"],
#     ["X", "X", "O"],
#     ["O", "X", "O"]
# ]

# print(check_winner(board))

#option 2
# def check_winner(board):
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2]:
#             return f"{row[0]} winner"

#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col]:
#             return f"{board[0][col]} winner"

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2]:
#         return f"{board[0][0]} winner"

#     if board[0][2] == board[1][1] == board[2][0]:
#         return f"{board[0][2]} winner"

#     return "Draw"


# # Input
# board = [
#     ["O", "O", "X"],
#     ["X", "X", "O"],
#     ["O", "X", "X"]
# ]

# print(check_winner(board))


#ques2
#option 1
# def find_indices(nums,target):
#     pair=[]
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 pair.append(i)
#                 pair.append(j)
#     return pair
# print(find_indices([11,2,15,7],9))

#option 2

# def find_indices(nums,target):
#     #start
#     if len(nums)==0:
#         return "Invalid input"
#     else:
#         result=[]
#         #two pointer
#         left=0
#         right=len(nums)-1
#         while left<right:
#             #finding the temporary sum of two numbers
#             temp=nums[left]+nums[right]
#             if temp < target:
#                 left+=1
#             if temp > target:
#                 right-=1
#             else:
#                 return[left,right]
            

# print(find_indices([2,7,11,15],9))
# print(find_indices([7,11,2,15],9))

# #In that test cases  it shows none message 
# print(find_indices([11,2,15,7],9))
# print(find_indices([15,11,2,7],9))

# def wordPattern(pattern, s):
#     words = s.split()

#     if len(pattern) != len(words):
#         return False

#     for i in range(len(pattern)):
#         # compare first occurrence positions
#         if pattern.index(pattern[i]) != words.index(words[i]):
#             return False

#     return True
# print(wordPattern("abba","dog cat cat dog"))
# print(wordPattern("abba", "dog cat dog cat"))


# def reverse_vowels(s):
#     vowels = "aeiouAEIOU"
#     s = list(s)

#     left = 0
#     right = len(s) - 1

#     while left < right:
        
        
#         while left < right and s[left] not in vowels:
#             left += 1

       
#         while left < right and s[right] not in vowels:
#             right -= 1

       
#         s[left], s[right] = s[right], s[left]

#         left += 1
#         right -= 1

    
#     result = ""
#     for char in s:
#         result += char

#     return result


# print(reverse_vowels("IceCreAm"))
# print(reverse_vowels("aeiou"))

