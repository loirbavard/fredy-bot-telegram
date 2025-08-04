# 🚀 Guide Simple - Déployer votre Bot Telegram

## 📋 Étape 1 : Créer un repository GitHub

1. **Allez sur** https://github.com
2. **Cliquez sur "Sign up"** (si vous n'avez pas de compte)
3. **Cliquez sur le bouton vert "New"** ou "New repository"
4. **Nommez-le** : `telegram-bot-fredy`
5. **Laissez tout par défaut**
6. **Cliquez sur "Create repository"**

## 📤 Étape 2 : Uploader vos fichiers

1. **Une fois le repository créé**, vous verrez une page avec des instructions
2. **Cliquez sur "uploading an existing file"** (lien bleu)
3. **Glissez-déposez** tous ces fichiers dans la zone :
   - `app.py`
   - `requirements.txt`
   - `render.yaml`
   - `README_RENDER.md`
4. **Cliquez sur "Commit changes"**

## 🚀 Étape 3 : Déployer sur Render

1. **Allez sur** https://render.com
2. **Cliquez sur "Sign Up"** et connectez-vous avec GitHub
3. **Cliquez sur "New +"** (bouton bleu)
4. **Sélectionnez "Web Service"**
5. **Connectez votre repository GitHub**
6. **Choisissez votre repository** `telegram-bot-fredy`
7. **Configurez** :
   - **Name** : `telegram-bot-fredy`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `python app.py`
8. **Cliquez sur "Create Web Service"**

## ⚙️ Étape 4 : Configurer le token

1. **Dans votre service Render**, allez dans l'onglet "Environment"
2. **Cliquez sur "Add Environment Variable"**
3. **Ajoutez** :
   - **Key** : `TELEGRAM_TOKEN`
   - **Value** : `8380142036:AAECByAZfHCR4tbnCsFMDIlpGWjvCUo2x14`
4. **Cliquez sur "Save Changes"**

## ✅ Étape 5 : Redéployer

1. **Allez dans l'onglet "Manual Deploy"**
2. **Cliquez sur "Deploy latest commit"**
3. **Attendez** que le statut devienne vert

## 🎯 Test final

1. **Ouvrez Telegram**
2. **Envoyez** `/start` à votre bot
3. **Il doit répondre** "Salut ! Ton bot fonctionne parfaitement 🚀"

## 🎉 C'est fini !

Votre bot fonctionne maintenant 24h/24 sur internet !

## 🆘 Si ça ne marche pas

- Vérifiez les logs dans Render (onglet "Logs")
- Assurez-vous que tous les fichiers sont uploadés
- Redéployez si nécessaire 