# 🚀 Déploiement du Bot Telegram sur Railway

## 📋 Prérequis
- Un compte GitHub
- Un compte Railway (gratuit)

## 🎯 Étapes de déploiement

### 1. **Créer un repository GitHub**

1. Allez sur https://github.com
2. Cliquez sur "New repository"
3. Nommez-le `telegram-bot-fredy`
4. Cliquez sur "Create repository"

### 2. **Uploader vos fichiers**

```bash
# Dans votre dossier D:\fredy
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/telegram-bot-fredy.git
git push -u origin main
```

### 3. **Déployer sur Railway**

1. **Allez sur** https://railway.app
2. **Connectez-vous avec GitHub**
3. **Cliquez sur "New Project"**
4. **Sélectionnez "Deploy from GitHub repo"**
5. **Choisissez votre repository** `telegram-bot-fredy`
6. **Cliquez sur "Deploy Now"**

### 4. **Configurer les variables d'environnement**

1. Dans Railway, allez dans votre projet
2. Cliquez sur l'onglet "Variables"
3. Ajoutez une variable :
   - **Nom** : `TELEGRAM_TOKEN`
   - **Valeur** : `8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14`

### 5. **Redéployer**

1. Allez dans l'onglet "Deployments"
2. Cliquez sur "Deploy Now"

## ✅ Vérification

1. **Vérifiez les logs** dans Railway
2. **Testez votre bot** sur Telegram avec `/start`
3. **Le bot fonctionne maintenant 24h/24 !**

## 🔧 Avantages de Railway

- ✅ **Gratuit** (500h/mois)
- ✅ **Démarrage automatique**
- ✅ **Redémarrage en cas de problème**
- ✅ **Logs en temps réel**
- ✅ **Variables d'environnement sécurisées**

## 🆘 Dépannage

### Le bot ne répond pas
1. Vérifiez les logs dans Railway
2. Vérifiez que le token est correct
3. Redéployez le projet

### Erreur de déploiement
1. Vérifiez que tous les fichiers sont uploadés
2. Vérifiez la syntaxe Python
3. Consultez les logs d'erreur

## 📞 Support

En cas de problème :
1. Vérifiez les logs Railway
2. Vérifiez la configuration du token
3. Testez localement avec `python app.py` 