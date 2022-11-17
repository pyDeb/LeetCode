regex="^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$|^([0-9]{3}-[0-9]{3}-[0-9]{4})$"
while read line; do
    [[ "$line" =~ $regex ]] && echo $line
done < "file.txt"
