#!/bin/bash
clear
echo "_____ Practice of if else statment ______"
read -p "Enter any name:" name
if [ $name = "dev" ];
then 
    echo "Welcome $name!"
else 
    echo "Who are you..?"
fi
