@echo off
set /p teste="Escolha o id de login (1,2,3): "
curl -X GET -d @familia%teste%.json https://acc-manager.southindia.cloudapp.azure.com/temfamilia --ssl-no-revoke --header "Content-Type:application/json"
pause