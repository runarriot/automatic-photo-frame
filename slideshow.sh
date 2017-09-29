#!/bin/sh
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
cat $SCRIPTPATH/data/db.txt | grep $1 | cut -d, -f1 > $SCRIPTPATH/data/playlist.txt
killall -9 feh
<<<<<<< HEAD
feh -FrZrD5 -f $SCRIPTPATH/data/playlist.txt
=======
feh -FrZrD5 -f $SCRIPTPATH/data/playlist.txt 
>>>>>>> f53cd18ba294e61f70995aaf4711d36d4febcc69
