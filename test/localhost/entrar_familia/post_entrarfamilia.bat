@echo off
set /p teste="Escolha o caso de teste (1, 2): "
curl -X POST -d @familia%teste%.json http://127.0.0.1:5000/entrarfamilia --header "Content-Type:application/json"