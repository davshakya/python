

# # txt =('a', 'a', 'a')
# # str1 =  '+'.join(txt)
# # print(str1)
# # a=2
# # b=3
# # c=4
# # d=5
# # e=6
# # f=7
# # g=8
# # h=9
# # i=10
# # j=11
# # y=eval(str1)
# # if(y<30):
# #     print(str1)


# def possibleStrings(n, r, b, g): 
      
#     # Store factorial of numbers up to n 
#     # for further computation 
#     fact = [0 for i in range(n + 1)] 
#     fact[0] = 1
#     for i in range(1, n + 1, 1): 
#         fact[i] = fact[i - 1] * i 
  
#     # Find the remaining values to be added 
#     left = n - (r + g + b) 
#     sum = 0
  
#     # Make all possible combinations of  
#     # R, B and G for the remaining value 
#     for i in range(0, left + 1, 1): 
#         for j in range(0, left - i + 1, 1): 
#             k = left - (i + j) 
  
#             # Compute permutation of each  
#             # combination one by one and add them. 
#             sum = (sum + fact[n] / (fact[i + r] * 
#                          fact[j + b] * fact[k + g])) 
      
#     # Return total no. of  
#     # strings/permutation 
#     return sum
  
# # # Driver code 
# if __name__ == '__main__': 
#     n = 11
#     r = 2
#     b = 0
#     g = 1
# #     print(int(possibleStrings(n, r, b, g))) 



# from itertools import combinations
# import pandas as pd

# Using skbrhmn's df
# df = pd.DataFrame({"Calories": [100, 200, 300, 400, 500],
#                    "Protein": [10, 20, 30, 40, 50],
#                    "IsBreakfast": [1, 1, 0, 0, 0],
#                    "IsLunch": [1, 0, 0, 0, 1],
#                    "IsDinner": [1, 1, 1, 0, 1]})

# comb_rows = list(combinations(df.index, 3))
# print(comb_rows)




import numpy as np
i, j = np.tril_indices(5, 1)
print(list(zip(i, j)))