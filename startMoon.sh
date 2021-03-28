#!/bin/sh

# Name of program in ps-list
NAME="MoonBot*"

# check if running
if ( ps -a | grep "$NAME" )
then
echo "$NAME is running..."
else
echo "$NAME NOT running! Restarting..."
python3 /home/pi/moonbot/MoonBot.py &
fi