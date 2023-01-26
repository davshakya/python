# d1 = {"a": 7, "b": 4, "c": {"x": 9, "y": [12, {"z": 78}, 33, 5, 6]}}
# print(d1["c"]["y"][1]["z"])
#
# d2={"a": 7, "b": 4, "c": 6}
#
# for key in d1["c"]["y"][1].keys():
#     print(key)


# n = 7
# l = []
# for i in range(1,n+1):
#     if n % i == 0:
#         l.append(i)
# print(l)
# if len(l)==2:
#     print("It is prime number")
# else:
#     print("It is composite number")

########String reverse#########
# s="devendra"
# r=""
# for i in range(len(s)):
#     r=s[i]+r
# print(r)

###########Reverse list#######

# l = [4, 67, 7, 6, 1, 10, 90, 2, 9,12 ]
# for i in range(len(l)):
#     for j in range(i):
#             l[i],l[j]=l[j],l[i]
# print(l)


###########Sorting list#######

# l = [4, 67, 7, 6, 1, 10, 90, 2, 9,12 ]
# for i in range(len(l)):
#     for j in range(i):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

###########Factorial#######

# n=int(input("Enter any number: "))
# if n==0:
#     print("Factorial of n =",1)
# else:
#     for i in range(1,n):
#         n=n*i
#     print("Factorial of n =",n)


