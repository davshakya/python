import numpy as np
import random
# l=[1,2,3,4,5]
# myarr=np.array(l)
# print(myarr)
# print(type(myarr))

# a=np.array()
# a=np.eye(3)
# print(a)


# i=[[1,2,3,4],[5,6,7,8],[9,8,7,8]]
# a=np.array(i)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(np.zeros((2,3)))
# print(np.ones((2,3)))
# print(np.eye(2))
# print(np.diag([2,3,4]))

a=np.random.randint(1,50,6)
print(a)

# a=np.random.rand(3)
# print(a)

# a=np.random.rand(3,3)
# print(a)

# a=np.random.randn(3)
# print(a)

# a=[]
# n=int(input("Enter any size of list="))
# for i in range(n):
#     j=a.append(int(input("Enter the element=")))
# # print(a)
# myarr=np.array(a)
# print(myarr)
# print(myarr.size)

# a=[4,7,8,4,9,6]
# myarr=np.array(a)
# print(myarr)
# print(myarr.size)
# sm=0
# for i in range(myarr.size):
#     sm=sm+myarr[i]
# print(sm)
# print(myarr[0:3])
# print(myarr[-2:-4:-1])

# a=np.random.randint(1,100,12)
# i=a.reshape(3,4)
# i=a.reshape(12) # 2d to 1d conversion
# i=a.reshape(2,2,3) # 2d to 3d conversion
# i=a.reshape(6,-1)
# print(i.ndim)
# print(i)


# np.random.seed(1)
# i=np.random.randint(1,100,12)
# print(i)

# row=int(input("Enter size of row="))
# col=int(input("Enter size of col="))
# mat=[]
# for i in range(row):
#     lst=[]
#     for j in range(col):
#         k=int(input("Enter the numbers="))
#         lst.append(k)     
#     mat.append(lst)
# print(mat)
# s=np.array(mat)
# print(s)
# print(type(s))

# l=[[3,5,3],[2,5,8],[5,7,3]]
# l=[6,7,5,3,3,2,4,4]
# a=np.array(l)
# print(a[:2])
# print(a[:2,1:4])
# b=a[:2,1:4]
# print(b)

# np.random.seed(1)
# a=np.random.randint(1,500,30).reshape(5,6)
# print(a) 
# mat=a[:3,1:3]
# print(mat)
# mat=a[3:5,3:6]
# print(mat)

# l=[3,4,5,2,4,5,]
# a=np.array(l)
# b=a[2:4].copy()
# b[:]=0
# print(a)

# l=[3,4,15,12,14,5,]
# b=np.array(l)
# print(b>10)

# b=np.arange(1,15)
# print(b>10)
# print(b[b>5])
# print(b[b%2==0])
# print(b[b%2!=0])
# b[b>6]=0
# print(b)

# ar=np.arange(10,19).reshape(3,3)
# br=np.arange(30,39).reshape(3,3)
# print(ar)
# print(ar*2)
# print(ar**2)
# print(ar/0)
# print(br)
# print(ar+br)
# print(ar=br)
# print(ar.dot(br))

# a=np.arange(1,10).reshape(3,3) 
# print(a)

# # a=lambda x,y:x+y
# # print(a(3,4))
# print(a.T)
# print(np.transpose(a))







