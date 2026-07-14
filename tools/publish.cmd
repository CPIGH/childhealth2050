@echo off
REM Double-click this to publish pending content changes to the live website.
REM (It just runs tools\publish.py and keeps the window open so you can read the result.)
python "%~dp0publish.py"
echo.
pause
