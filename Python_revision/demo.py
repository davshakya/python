# n = 100

# p=[]
# for j in range(1, n+1):
#     k=[]
#     for i in range(1, j+1):
#         if j%i==0:
#             k.append(i)
#     if len(k) == 2:
#             p.extend(k[1:2])            
# print(p)


# st= "Devendra Singh Shakya"
# # st= "Devendra"

# rev1=''
# for j in st.split():
#     rev=""
#     for i in j:
#         rev = i+rev
#     rev1= rev1 +" "+ rev
            
# print(rev1)

# a=2
# b=3
# c=2


# if a>=b and b>=c:
#     print('a',a)
# elif b>=a and b>=c:
#     print('b',b)
# elif c>=a and c>=b:
#     print("c", c)
    
    
# def fibonacci(n):
#     lt=[0,1]
#     while len(lt)<n:
#         lt.append(lt[-1]+lt[-2])
#     return lt
# print(fibonacci(10))


# def fibonacci(n):
#     x=0
#     y=1
#     for i in range(n):
#         yield x
#         x,y=y,x+y

# print(list(fibonacci(10)))




