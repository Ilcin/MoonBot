#!/bin/bash
# Name of program in ps-list
if ( ps -x | grep "[M]oonBot.py" )
    then echo "Moonbot is running..."
    else nohup python -u /home/pi/moonbot/startup.py &
fi