@echo off
set /p teste="Escolha o caso de teste (1, 2, 3): "
curl -X POST -d @login%teste%.json https://acc-manager.southindia.cloudapp.azure.com/login --ssl-no-revoke --header "Content-Type:application/json"
pause