#!/bin/sh

echo "Starting Batch Autograding"

# files to be checked
F1=search.py
F2=searchAgents.py

# delete grades.txt file before starting
rm -f grades.txt

#delete previous files that need to be checked
rm -f $F1 $F2

for d in ./files/* ; do
    echo "$d"
    FL=$d/$F1
    if [ ! -f "$FL" ]; then   # check if F1 exists, if not then continue to next folder
        echo "$F1 does not exist"
        continue
    fi

    FL=$d/$F2
    if [ ! -f "$FL" ]; then   # check if F2 exists, if not then continue to next folder
        echo "---->$F2 does not exist"
        continue
    fi
        
    # copy files to main folder for checking
    cp -f $d/$F1 ./
    cp -f $d/$F2 ./

    echo "Running autograder ..."
        
    # run autograder and update grades.txt file
    MARK=$(python autograder.py | grep -w "Total:" | cut -d " " -f 2)
    STD=$(echo "$d" | cut -d "/" -f 3)

    echo "$STD" "$MARK" >> grades.txt

    # delete files again to start fresh in the new loop
    rm -f $F1 $F2

done

echo "Autograding Complete. Check the grades in grades.txt file."
