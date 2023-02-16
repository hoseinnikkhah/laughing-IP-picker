@echo off
for /f "tokens=1 delims= " %%a in ('curl http://bot.sudoer.net/best.cf.iran.all') do (
echo %%a>>ipraw.txt
)
start "executed.exe"
pause