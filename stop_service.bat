@echo off
echo Arrêt et désinstallation du service Telegram Bot...
echo.

REM Arrêter le service
echo Arrêt du service...
python bot_service.py stop

REM Désinstaller le service
echo Désinstallation du service...
python bot_service.py remove

echo.
echo Service arrêté et désinstallé avec succès!
echo.
pause 