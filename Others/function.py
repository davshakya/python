# # def cmb(x, y):
# #     if not x: 
# #         return
# #     y.add(x)
# #     for z in range(0, len(x)):
# # #         t = x[0:z] + x[z + 1:]
# # #         cmb(t,y)
# # # y = set()
# # # cmb("abc", y) 
# # # t=list(y)
# # # print(t)

# # def cmb(x, y):
# #     if not x: 
# #         return
# #     y.add(x)
# #     for z in range(0, len(x)):
# #         t = x[0:z] + x[z + 1:]
# #         cmb(t,y)
# # y = set()
# # cmb("abc", y) 
# # # t=list(y)
# # # for i in range (0,len(t)):
# # #     abc_dict={ "a": 2, "b":3, "c":4}
# # #     a=2
# # #     b=3
# # #     c=4 
# # #     d=5
# # #     numbers=[a,bc,cd,d] 
# # #     Sum = sum(numbers) 
# # #     print(Sum) 
# # #         if t[i] in abc_dict:
# # #             print(t[i])

# # for i in range(97,123):
# #     print(chr(i), end=" ")'

# # operator. add(x, y)'


# def sum_digits_string(str1):
#     sum_digit = 0
#     for x in str1:
#         if x.isdigit() == True:
#             z = int(x)
#             sum_digit = sum_digit + z

#     return sum_digit
     
# print(sum_digits_string("123abcd45"))
# print(sum_digits_string("abcd1234"))


def cmb(x, y):
    if not x: 
        return
    y.add(x)
    for z in range(0, len(x)):
        t = x[0:z] + x[z + 1:]
        cmb(t,y)       
y = set()
cmb("abc123", y) 
t=list(y)
def sum_str(str1):
    sum_dgt = 0
    for x in str1:
        # if x.isdigit() == True:
            z = int(x)
            z = str(x)
            a=2
            b=3
            c=4
            sum_dgt = sum_dgt + z

    return sum_dgt
     
print(sum_str(t))








