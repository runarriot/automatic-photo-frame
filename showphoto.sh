#!/bin/sh
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
sudo killall fbi
sudo fbi -noverbose -T 1 -fitwidth  $1 
