@echo off
set /p teste="Escolha o caso de teste (1, 2, 3): "
curl -X POST -d @cadastro%teste%.json https://acc-manager.southindia.cloudapp.azure.com/cadastrar --ssl-no-revoke --header "Content-Type:application/json"
pause