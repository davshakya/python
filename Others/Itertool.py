# a=input("Enter first letter >>")
# b=input("Enter second letter >>")
# c=input("Enter third letter >>")

# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range (0,3):
#     for j in range (0,3):
#         for k in range (0,3):
#                 if(i!=j & j!=k & k!=i):
#                     x=int(d[i])
#                     y=int(d[j])
#                     z=int(d[k])
#                     w=x+y+z
                    
#                     if (w>20):
#                         print("sorry")
#                     else:
#                         print(d[i],d[j],d[k])



# # list1 = [11, "a", 17, 18, 23] 
  
# # # using sum() function 
# # # total = concat(list1) 
  
# # # # # printing total value 
# # # # print("Sum of all elements in given list: ", total)

# # # txt = ("banana")

# # # x = txt.split(" ")

# # # print(x)
# # # x="abcd"
# # # for z in range(0, len(x)):
# # #         t = x[0:z] + x[z + 1:]
# # #         abc_dict={ "a": 2, "b":3, "c":4}
# # #         for i in range (0,len(t)):
# # #                 if t[i] in abc_dict:
# # #                         print(t[i])
# # def Sum(abc_dict): 
# #      sum = 0
# #      for i in dict.values(): 
# #            sum = sum + i 
# #      return sum
# # abc_dict1 = {'a': 2, 'b':3, 'c':4} 
# # print("Sum :", Sum(abc_dict))
# x=0
# for i in range(0,3):
#         x=x+1
#         print(x)

# sum = 0
# abc_dict={ "a": 2, "b":3, "c":4}
# for i in abc_dict: 
#         sum = sum + abc_dict[i] 
#         print(sum)

# for z in range(0, len(x)):
#         t = x[0:z] + x[z + 1:]
#         for i in abc_dict: 
#                 sum = sum + abc_dict[i] 

# def returnSum(myDict): 
      
#     return sum
  
# # Driver Function 

# abc_dict={ "a": 2, "b":3, "c":4}
# # print(abc_dict["a"])

def cmb(x, y):
    if not x: 
        return
    y.add(x)
    for z in range(0, len(x)):
        t = x[0:z] + x[z + 1:]
        cmb(t,y)       
y = set()
cmb("abcde", y) 
t=list(y)
print(t)

a=2
b=3
c=4 
d=5
e=6
numbers=[a,b,c,d,e] 
Sum = sum(numbers) 
if(Sum<40):
        print(Sum) 
else:
        print("Out of range")
a_dict = {"a":2, "b":3, "c": 4}
values = a_dict.values()
total = sum(values)
print(total)


