# def greater_than_5(num):
#     if num>5:
#         return True
#     else:
#          return False
greater_than_5=lambda num:num>5
l=[1,2,3,4,5,5,6,8,3]
print(list(filter(greater_than_5,l)))

a=filter(lambda a:a%5==0,l)
print(list(a))