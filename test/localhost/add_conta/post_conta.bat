@echo off
set /p teste="Escolha o caso de teste (1, 2, 3, 4): "
curl -X POST -d @conta%teste%.json http://127.0.0.1:5000/addconta --header "Content-Type:application/json"
pause