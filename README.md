# Bot Telegram Fredy - Configuration Permanente

## 🚀 Installation du Service Windows

### Prérequis
- Python 3.7 ou plus récent
- Windows 10/11

### Étapes d'installation

1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

2. **Installer et démarrer le service** :
   - Double-cliquez sur `install_service.bat`
   - Ou exécutez en tant qu'administrateur

3. **Vérifier que le service fonctionne** :
   - Ouvrez "Services" (services.msc)
   - Cherchez "Telegram Bot Service"
   - Le statut doit être "En cours d'exécution"

### Commandes utiles

**Démarrer le service manuellement** :
```bash
python bot_service.py start
```

**Arrêter le service** :
```bash
python bot_service.py stop
```

**Désinstaller le service** :
```bash
python bot_service.py remove
```

**Vérifier le statut** :
```bash
python bot_service.py status
```

## 🔧 Configuration

### Modifier le token
Éditez le fichier `bot_service.py` et changez la ligne :
```python
TOKEN = "votre_nouveau_token_ici"
```

### Ajouter de nouvelles commandes
Modifiez la fonction `run_bot()` dans `bot_service.py` pour ajouter vos commandes.

## 📝 Logs

Les logs du service sont disponibles dans :
- Événements Windows (Event Viewer)
- Application > Services > Telegram Bot Service

## ⚠️ Notes importantes

1. **Exécution en tant qu'administrateur** : L'installation du service nécessite des droits administrateur
2. **Démarrage automatique** : Le service se lancera automatiquement au démarrage de Windows
3. **Sécurité** : Gardez votre token secret et ne le partagez jamais

## 🆘 Dépannage

### Le service ne démarre pas
1. Vérifiez que Python est installé et dans le PATH
2. Vérifiez que toutes les dépendances sont installées
3. Exécutez en tant qu'administrateur

### Le bot ne répond pas
1. Vérifiez que le token est correct
2. Vérifiez la connexion internet
3. Consultez les logs dans l'Observateur d'événements

## 📞 Support

En cas de problème, vérifiez :
1. Les logs Windows
2. La configuration du token
3. La connectivité réseau 