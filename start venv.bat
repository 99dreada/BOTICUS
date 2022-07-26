@ECHO OFF
CLS
call "venv/Scripts/activate.bat"

:begin
CLS
ECHO 1.Full Setup (Run this if first time setup)
ECHO 2.Install requirements
ECHO 3.Build DB
ECHO 4.Run Application
ECHO.
CHOICE /C 1234 /M "Enter your choice:"

IF ERRORLEVEL 4 GOTO Run
IF ERRORLEVEL 3 GOTO Builddb
IF ERRORLEVEL 2 GOTO Install
IF ERRORLEVEL 1 GOTO Fullsetup

:Fullsetup
Echo Installing dependancy
pip install -r requirements.txt
ECHO Setting up database
flask db init
ECHO Setup complete
pause
GOTO begin

:Install
Echo installing BOTICUS dependancy
pip install -r requirements.txt
pause
GOTO begin

:Builddb
ECHO Setting up BOTICUS database
flask db init
pause
GOTO begin

:Run
Echo Application will now start
cd /BOTICUS
flask run

:exit
@exit