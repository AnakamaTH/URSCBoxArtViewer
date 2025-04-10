@echo off
echo Building URSC Box Art Viewer...
pip install pyinstaller pillow >nul
pyinstaller URSC_BoxArt.py --onefile --version-file=version.txt --icon=sonic.ico 
pause
