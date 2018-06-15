#!/bin/sh
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
cat $SCRIPTPATH/data/db.txt | grep -i $1 | cut -d, -f1 > $SCRIPTPATH/data/playlist.txt
imgcnt=$(cat  $SCRIPTPATH/data/playlist.txt | wc -l)
if [ ${imgcnt} -gt 0 ]
then
	sudo killall -9 fbi
	sudo fbi -T 1 -u -t 20 -noverbose -fitwidth -l  $SCRIPTPATH/data/playlist.txt
fi


