# 🚀 Déploiement du Bot Telegram sur Replit

## 📋 Prérequis
- Un compte Replit (gratuit)

## 🎯 Étapes de déploiement (Très simple !)

### 1. **Créer un compte Replit**
1. **Allez sur** https://replit.com
2. **Cliquez sur "Sign Up"**
3. **Créez un compte gratuit**

### 2. **Créer un nouveau projet**
1. **Cliquez sur "Create Repl"**
2. **Choisissez "Python"**
3. **Nommez-le** `fredy-bot`
4. **Cliquez sur "Create Repl"**

### 3. **Uploader les fichiers**
1. **Supprimez** le fichier `main.py` existant
2. **Cliquez sur "Upload file"**
3. **Uploadez** :
   - `app.py`
   - `requirements.txt`
4. **Renommez** `app.py` en `main.py`

### 4. **Configurer les variables d'environnement**
1. **Cliquez sur "Tools"** (à gauche)
2. **Cliquez sur "Secrets"**
3. **Ajoutez** :
   - **Key** : `TELEGRAM_TOKEN`
   - **Value** : `8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14`

### 5. **Démarrer le bot**
1. **Cliquez sur "Run"** (bouton vert)
2. **Le bot démarre automatiquement !**

## ✅ Vérification

1. **Regardez la console** (à droite)
2. **Vous devriez voir** : "Bot démarré sur Replit..."
3. **Testez votre bot** sur Telegram avec `/start`

## 🔧 Avantages de Replit

- ✅ **Gratuit**
- ✅ **Interface très simple**
- ✅ **Pas besoin de Git**
- ✅ **Déploiement en 1 clic**
- ✅ **Console en temps réel**

## 🆘 Dépannage

### Le bot ne démarre pas
1. Vérifiez que `main.py` contient le bon code
2. Vérifiez que le token est correct dans Secrets
3. Regardez les erreurs dans la console

### Erreur de module
1. Vérifiez que `requirements.txt` est présent
2. Replit installe automatiquement les dépendances

## 📞 Support

En cas de problème :
1. Regardez la console Replit
2. Vérifiez la configuration du token
3. Redémarrez avec le bouton "Run" 