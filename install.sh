#!/bin/bash

# Create venv if not existing
if [[ ! -d "venv" ]]
then
  echo "[Install] Creating new venv: venv"
  python3 -m venv venv
  if [[ 0 -ne "$?" ]]
  then
    echo "[Install] Install failed"
    exit 1
  fi
fi

# Select the venv
source venv/bin/activate

# Check if dependecies are installed
python3 -c "import colorama" > /dev/null 2>&1
if [[ 1 -eq "$?" ]]
then
  echo "[Install] Downloading colorama"
  pip3 install colorama
  if [[ 0 -ne "$?" ]]
  then
    echo "[Install] Install failed"
    # Deactivate venv
    deactivate
    exit 1
  fi
fi

# Deactivate venv
deactivate

echo "[Install] Install finished"
exit 0
