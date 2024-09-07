#!/bin/bash
clear 
read -p "Enter  any file name:" fname
if [ -a $fname ];
then 
    echo "File is exist.."
else
    echo "File not exist.."
fi     