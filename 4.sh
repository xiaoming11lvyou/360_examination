#!/bin/sh
#日志切割　:每INTERNAL=10min检查一次，如果文件大于MAX =1000kbytes,则切割并清空源文件
#切割生成文件以时间.log命名
MAX=1000
INTERVAL=10m
filename=access.log
detect ()
{
         if [ $1 -gt $MAX ]
         then
         echo true
         else 
         echo false
         fi
}
while $(detect $(du $filename))
do
newfilename=$(date +"%Y%m%d-%H:%M:%S").log
cp $filename $newfilename
echo "">$filename
sleep $INTERVAL 
done
