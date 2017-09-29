# automatic-photo-frame
Linux based automatic photo frame - controlled from any device on the net - auto on/off - auto playlists etc.

The idea is to recover memories from previous years - auto playlists based on actual time - ie if its summer it shows photos from previous summers.. same with xmas etc.. 
Playlists can also be controlled - if you want, just type a message on your phone to  show photos you are inrested in :)

...::WIP::..

## Current features video

[![automatic photo frame video](https://img.youtube.com/vi/R3AQWtuPeqg/0.jpg)](https://youtu.be/R3AQWtuPeqg)
- left side is your phone anywhere with internet, 
- right side is yours photo frame connected to wifi

## What is working?
- bot commands:
    - refreshdb
        - runs refreshdb script - it makes csv with filename createdate and keywords
    - show 'keyword'
        - greps db file for keyword and add all matching files to playlist and launch feh in fullscreen
    - display photo sent via telegram chat
        - send any photo to the frame via telegram messenger and it will be displayed on the frame

## To do next
- startup script (.xprofile)
- cron config for daily refreshdb & auto playlists generator

## Main goals
- automatic daily playlists from previous years (same time +/- few days to fit some photo limit )
- control via telegram:
    - create playlist - msg: show vacation 2017 - queries photo tags and if matched add to playlist
    - change change photo delay 
    - photo to frame from phone
    - random photos from web galleries
- working schedule on/off in speciied time
- option: enable screen only when somebody is at home - query wifi network if phone is connected.

## Requirements
- linux (raspbian, ubuntu ... )
- exiftool
- python & pip install pyTelegramBotAPI
- feh & xserver - option is fbi (framebuffer image viewer - but X session has more features for future use.. )

## Configuration
- edit config.json and change telegram bot token
