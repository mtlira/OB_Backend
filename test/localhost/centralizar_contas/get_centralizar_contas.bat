@echo off
set /p teste="Escolha o caso de teste (1,2,3): "
curl -X GET -d @login%teste%.json http://127.0.0.1:5000/centralizarcontas --header "Content-Type:application/json"