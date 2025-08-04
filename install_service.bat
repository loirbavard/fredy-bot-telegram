@echo off
echo Installation du service Telegram Bot...
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installé ou n'est pas dans le PATH
    pause
    exit /b 1
)

REM Installer les dépendances
echo Installation des dépendances...
pip install -r requirements.txt

REM Installer le service
echo Installation du service...
python bot_service.py install

REM Démarrer le service
echo Démarrage du service...
python bot_service.py start

echo.
echo Service installé et démarré avec succès!
echo Le bot fonctionne maintenant en permanence.
echo.
echo Pour arrêter le service: python bot_service.py stop
echo Pour désinstaller le service: python bot_service.py remove
echo.
pause 