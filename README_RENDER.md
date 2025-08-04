# 🚀 Déploiement du Bot Telegram sur Render

## 📋 Prérequis
- Un compte GitHub
- Un compte Render (gratuit)

## 🎯 Étapes de déploiement

### 1. **Créer un repository GitHub**

1. Allez sur https://github.com
2. Cliquez sur "New repository"
3. Nommez-le `telegram-bot-fredy`
4. Cliquez sur "Create repository"

### 2. **Uploader vos fichiers**

```bash
# Dans PowerShell, naviguez vers D:\fredy
cd "D:\fredy"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/telegram-bot-fredy.git
git push -u origin main
```

### 3. **Déployer sur Render**

1. **Allez sur** https://render.com
2. **Cliquez sur "Sign Up"** et connectez-vous avec GitHub
3. **Cliquez sur "New +"**
4. **Sélectionnez "Web Service"**
5. **Connectez votre repository GitHub**
6. **Choisissez votre repository** `telegram-bot-fredy`
7. **Configurez le service** :
   - **Name** : `telegram-bot-fredy`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `python app.py`
8. **Cliquez sur "Create Web Service"**

### 4. **Configurer les variables d'environnement**

1. Dans votre service Render, allez dans "Environment"
2. Ajoutez une variable :
   - **Key** : `TELEGRAM_TOKEN`
   - **Value** : `8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14`
3. Cliquez sur "Save Changes"

### 5. **Redéployer**

1. Allez dans l'onglet "Manual Deploy"
2. Cliquez sur "Deploy latest commit"

## ✅ Vérification

1. **Vérifiez les logs** dans Render
2. **Testez votre bot** sur Telegram avec `/start`
3. **Le bot fonctionne maintenant 24h/24 !**

## 🔧 Avantages de Render

- ✅ **Gratuit** (750h/mois)
- ✅ **Démarrage automatique**
- ✅ **Redémarrage en cas de problème**
- ✅ **Logs en temps réel**
- ✅ **Variables d'environnement sécurisées**
- ✅ **Interface simple et intuitive**

## 🆘 Dépannage

### Le bot ne répond pas
1. Vérifiez les logs dans Render
2. Vérifiez que le token est correct
3. Redéployez le service

### Erreur de déploiement
1. Vérifiez que tous les fichiers sont uploadés
2. Vérifiez la syntaxe Python
3. Consultez les logs d'erreur

### Service s'arrête automatiquement
1. Render arrête les services inactifs après 15 minutes
2. Le bot redémarre automatiquement quand il reçoit un message
3. C'est normal pour le plan gratuit

## 📞 Support

En cas de problème :
1. Vérifiez les logs Render
2. Vérifiez la configuration du token
3. Testez localement avec `python app.py`

## 🎯 Commandes utiles

```bash
# Vérifier les logs
# Allez dans Render > Votre service > Logs

# Redéployer
# Render > Votre service > Manual Deploy > Deploy latest commit
``` 