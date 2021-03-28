#!/bin/sh
# Name of program in ps-list
NAME="MoonBot.py"
# check if running
if ( ps -a | grep "$NAME" ) then 
    echo "$NAME is running..." 
else 
    echo "$NAME NOT running! Restarting..." 
    nohup python -u /home/pi/moonbot/startup.py & 
fi