from itertools import permutations 
str="abcdefghijklmnopqrstuvwxyz"
y=int(input("Enter range of letters of alphabet ="))
your_str=str[0:y]
print("You entered  =", your_str) 
m=int(input("How many string do you want? ="))
r=int(input("Enter range of letters Combination ="))
permutation = [''.join(x) for x in permutations(your_str,r)] 
x=tuple(permutation)
print(', '.join(x[0:m]))
















