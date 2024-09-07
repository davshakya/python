clear
read -p "Enter the name:" name
read -p "Enter the age:" age

if [ $name="Dev" -a $age -ge 18 ];
then
    echo "You are eligible for all stuff."
else 
    echo "Your age is less than 18, Dont worry you are eligible for some limited stuff."
fi 