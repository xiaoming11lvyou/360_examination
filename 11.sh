#!/bin/sh
#假设已经能够免密码登陆，且每次输入命令如果有空格需加引号
while read temp
do 
for comm in $@
do
ssh $comm
$temp
exit
exit
done
done
