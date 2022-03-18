n=`cat file.txt | wc -l`
if ((n >= 10));
then
    cat file.txt | head -10 | tail -1
fi
