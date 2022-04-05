@echo off
set /p token=<../../jwt.txt
set /p teste="Escolha o id de login (1,2,3): "
curl -X GET -d @familia%teste%.json http://127.0.0.1:5000/temfamilia --header "Content-Type:application/json" --header "%token%"