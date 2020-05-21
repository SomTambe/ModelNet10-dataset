cd ./monitor
# alias "binvox"="~/Desktop/binvox"
for f in *.off
do 
    ~/Desktop/binvox $f -d 32 -e -cb
done