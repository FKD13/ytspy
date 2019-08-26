#!/bin/zsh

# Enter venv
source venv/bin/activate

# Make sure music.fifo exists
if [[ ! -e music.fifo ]]
then
  mkfifo music.fifo
fi

# Enable video playback
VIDEO="--no-vid"
if [[ "$1" == "--video" ]]
then
  VIDEO=""
fi

# Create a new mpv process that runs in backgound
mpv $VIDEO --force-window=yes --input-file=music.fifo --idle > mpv.log 2>&1 &

# Grab the mpv process so we can kill it later
PROCESS=$(ps | grep 'mpv' | sed -E 's/^ *([0-9]+) .*$/\1/')

# Start the music searcher
./main.py

# Kill the mpv process
kill $PROCESS

# Exit venv
deactivate

# Exit ok
exit 0
