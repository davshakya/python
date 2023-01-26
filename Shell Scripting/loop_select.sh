select data in apple cow rose
do 
    if [ "$data" = apple ];
    then 
        echo "You have selected a fruit."
    elif [ "$data" = cow ];
    then 
        echo "You have selected a animal."
    elif [ "$data" = rose ];
    then 
        echo "You have selected a flower."
    else
        echo "Wrong selection"
        break
    fi
done 