@echo OFF

echo checking for pakages needing to be installed

pip install pytube
pip install PySimpleGUI
pip install rich

echo =============DONE=============
echo starting the program

python3 main.py