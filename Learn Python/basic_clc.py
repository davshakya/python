print('''
      + Addition
      - Subtraction
      / Devide
      * Multiply''')

num1=int(input("Enter any first number: "))
num2=int(input("Enter any first number: "))
opr=input("Enter operator symbol: ")
if opr=="+":
    print(num1+num2)    
elif opr=="-":
    print(num1-num2)    
elif opr=="/":
    print(num1/num2)    
elif opr=="*":
    print(num1*num2)    
else:
    print("Invalid operator choosed" )
