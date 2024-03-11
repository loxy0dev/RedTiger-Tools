title Red Tiger - Installation of modules.
@echo off
cls
echo Installing the python modules required for the Red Tiger Tool:
timeout /t 5 /nobreak > nul
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip

pip install time
pip install selenium
pip install colorama
pip install requests
pip install json
pip install random
pip install string
pip install ctypes
pip install base64
pip install threading
pip install psutil
pip install bs4
pip install webbrowser
pip install itertools
pip install phonenumbers
echo Finish.
start Start.bat
