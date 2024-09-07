clear
read -p "Enter your name:" name
echo "Hello $name ! "

echo "Script for Arthmetic Operators of two numbers"
x=7
y=8
add=$(($x+$y))
echo "sum of two number is: $add"

read -p "Enter the value of x,y:" x y
read -p "Enter the value of y:" y
add=$(($x+$y))
echo "Sum of two number is: $add"

sub=$(($x-$y))
echo "Subtraction of two number is: $sub"

sub=$(($x*$y))
echo "Multiply of two number is: $sub"

sub=$(($x/$y))
echo "Division of two number is: $sub"

sub=$(($x%$y))
echo "Modulus of two number is: $sub"
