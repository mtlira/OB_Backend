@echo off
set /p teste="Escolha o caso de teste (1, 2, 3): "
curl -X POST -d @login%teste%.json http://127.0.0.1:5000/login --header "Content-Type:application/json"
pause