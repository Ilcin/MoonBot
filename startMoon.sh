#!/bin/bash
# Name of program in ps-list
NAME="MoonBot.py"
if ( ps -x | grep "MoonBot.py" )
    then echo "Moonbot is running..."
    else nohup python -u /home/pi/moonbot/startup.py &
fi