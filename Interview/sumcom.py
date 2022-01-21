# def permute(nums):
#   result_perms = [[]]
#   for n in nums:
#     new_perms = []
#     for perm in result_perms:
#       for i in range(len(perm)+1):
#         new_perms.append(perm[:i] + [n] + perm[i:])
#         result_perms = new_perms
#   return result_perms

# my_nums = "123"
# print("Original Cofllection: ",my_nums)
# t=list(permute(my_nums))
# print(t)

# for k in range (len(t)):
#   # print(t[k])

#   for i in range (len(k)):
#     j=str(t[i])
#     def sum_str(str1):
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt
#     m=sum_str(t[i])

import itertools
def prmt(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms
my_nums = "1234"
print("Entered String: ",my_nums)
t=list(prmt(my_nums))
print(t)

for i in range (len(t)):
 j=str(t[i])
 def sum_str(str1):
        sum_dgt = 0
        for x in str1:
            if x.isdigit() == True:
                z = int(x)
                sum_dgt = sum_dgt + z
        return sum_dgt
m=sum_str(t[i])

for i in range (len(t)):
  if(m<10):
      print(*t[i])
      for j in range (len(t)):
          values = t[i]
          com = itertools.combinations_with_replacement(values, 3)
          for val in com:
              print(*val)

# for i in range (len(val)):
#  j=str(val[i])
#  def sum_str(str1):  
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt
#  m=sum_str(t[i])
#  if (m<10):
#   print(*val)

# for i in range (len(val)):
#  j=str(val[i])
#  def sum_str(str1):  
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt
#  m=sum_str(t[i])
#  print(m)















