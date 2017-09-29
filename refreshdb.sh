#!/bin/sh
exiftool -csv -DateTimeOriginal -d %Y_%m%d -Keywords -XPKeywords $1 -r > $2 