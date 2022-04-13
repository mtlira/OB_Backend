@echo off
set /p email="email: "
set /p senha="senha: "
curl -X POST -d '{"email":"%email%","senha":"%senha%"}' https://acc-manager.southindia.cloudapp.azure.com/mangobank-back/login --ssl-no-revoke --header "Content-Type:application/json"
pause