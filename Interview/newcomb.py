from itertools import combinations 
from itertools import permutations 

import itertools
def rSubset(arr, r): 
    return list(permutations(arr, r)) 
if __name__ == "__main__": 
    # str2 =list(input("Enter any letter>>" ))
    str2 ="abcd"
    arr=str2
    # r = int(input("Enter target value>> "))
    r = 3

    m=rSubset(arr, r)
for j in range(len(m)):
    txt =m[j]
    str1 =  '+'.join(txt)
    a=8.5
    b=8.5
    c=9
    d=9
    e=9.5
    f=9.5
    g=10
    h=10
    i=10.5
    j=10.5
    k=11
    l=11
    # m=11
    # n=11.5
    # o=12
    # p=12
    # q=12.5
    # r=12.5
    # s=13
    # t=13
    # u=13.5
    # v=13.5
    y=eval(str1)
    if(y<26.5):
        # print(*txt)
        print(f"{txt}=",y)
        # print("Total Combination is =",len(txt))











