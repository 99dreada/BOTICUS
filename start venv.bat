@ECHO OFF
CLS
call "venv/Scripts/activate.bat"

:menu1
CLS
ECHO 1.Full Setup (Run this if first time setup ONLY)
ECHO 2.Run application options
ECHO.
CHOICE /C 12 /M "Enter your choice:"

IF ERRORLEVEL 2 GOTO menu2
IF ERRORLEVEL 1 GOTO Fullsetup

:menu2
CLS
ECHO 1.Run Application
ECHO 2.Build DB
ECHO 3.Install requirements.txt
ECHO 4.Set venv variables
ECHO 5.Start venv ("run if (venv) isnt at the start of command line")
ECHO.
CHOICE /C 12345 /M "Enter your choice:"

IF ERRORLEVEL 5 GOTO Startenv
IF ERRORLEVEL 4 GOTO Envsetup
IF ERRORLEVEL 3 GOTO Install
IF ERRORLEVEL 2 GOTO Builddb
IF ERRORLEVEL 1 GOTO Run


:Fullsetup
ECHO Installing pip
py -m pip install --upgrade pip
ECHO Installing venv
py -m pip install virtualenv
ECHO Creating venv
py -m venv venv
ECHO Starting enviroment
.\venv\Scripts\activate
ECHO Installing dependancy
pip install -r requirements.txt
set FLASK_APP=BOTICUS
set FLASK_DEBUG=1
ECHO Setting up DB
flask db init
GOTO menu1

:Builddb
ECHO Setting up BOTICUS database
flask db init
pause
GOTO menu2

:Install
Echo installing BOTICUS dependancy
pip install -r requirements.txt
pause
GOTO menu2

:Run
Echo Application will now start
flask run
if  errorlevel 1 goto ERROR

:Envsetup
ECHO Setting up enviroment
set FLASK_APP=BOTICUS
set FLASK_DEBUG=1
pause
GOTO menu2

:Startenv
ECHO Starting enviroment
.\venv\Scripts\activate
GOTO menu2

:exit
@exit

:ERROR
echo Failed
cmd /k
exit /b 1