#!/bin/sh
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
killall -9 feh
feh -FrZrD5  $1 