@echo off
set /p token=<../../jwt.txt
curl http://127.0.0.1:5000/temfamilia --header "x-access-token:%token%"