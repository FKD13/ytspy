#!/bin/zsh

# Make sure music.fifo exists
if [[ ! -e music.fifo ]]
then
  mkfifo music.fifo
fi

# Create a new mpv process that runs in backgound
mpv --input-file=music.fifo --idle > mpv.log 2>&1 &

# Grab the mpv process so we can kill it later
PROCESS=$(ps | grep 'mpv' | sed -E 's/^ *([0-9]+) .*$/\1/')

# Start the music searcher
./main.py

# Kill the mpv process
kill $PROCESS

# Exit ok
exit 0
