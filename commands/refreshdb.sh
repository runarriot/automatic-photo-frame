#!/bin/sh
exiftool -csv -DateTimeOriginal -d %Y_%m%d -Keywords $1 -r > $2
