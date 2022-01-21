
def even_odd(lst):
    # print(lst[0])
    cnt_odd=0
    cnt_even=0
    for k in range (0,len(lst)):
       if(lst[k]%2==0):
           cnt_even=cnt_even+1
       else:
           cnt_odd=cnt_odd+1
        # print(lst[k])
    print("Count of even number is= ",cnt_even)
    print("Count of odd number is= ",cnt_odd)
    
lst=[2,3,4,5,6,7,8,9,10]
even_odd(lst)


