@echo off
echo Installing required modules...

rem Download get-pip.py to install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

rem Use pip to install required modules
python -m pip install pillow requests

echo Running the application. Do not close this console or the application will close.
python -c "import tkinter as ihateapples"
python -c "from PIL import Image, ImageTk"
python -c "import io"
python -c "import requests"

rem Check if main.py exists, if not, run anivyle.exe
if exist main.py (
    python main.py
) else (
    start anivyle.exe
)

rem Cleanup: Delete get-pip.py
del get-pip.py
