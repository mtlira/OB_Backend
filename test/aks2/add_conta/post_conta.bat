@echo off
set /p teste="Escolha o caso de teste (1, 2, 3, 4): "
curl -X POST -d @conta%teste%.json https://acc-manager.southindia.cloudapp.azure.com/addconta --ssl-no-revoke --header "Content-Type:application/json"
pause