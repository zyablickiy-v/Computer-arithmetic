rem pyinstaller -w -F --add-data "wgui;wgui" main.py
pyinstaller -w --add-data "wgui;wgui" --icon=dev_wgui\public\favicon.ico main.py