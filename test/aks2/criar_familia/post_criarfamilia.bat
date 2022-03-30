@echo off
set /p teste="Escolha o caso de teste (1, 2): "
curl -X POST -d @familia%teste%.json https://acc-manager.southindia.cloudapp.azure.com/criarfamilia --ssl-no-revoke --header "Content-Type:application/json"
pause