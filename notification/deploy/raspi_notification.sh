#! /bin/bash

export PW_DEV_GAMIL='ENTER PASSWORD'

python3 -m venv /home/pi/workspace/raspi_scripts/notification/venv
source /home/pi/workspace/raspi_scripts/notification/venv/bin/activate
python /home/pi/workspace/raspi_scripts/notification/main.py
