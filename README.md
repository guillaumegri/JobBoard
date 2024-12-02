# JobBoard
Ce projet est une application interactive développée avec **Streamlit** permettant d'afficher des offres d'emploi issues d'API gratuites telles que **Remote OK**, et potentiellement d'autres sources comme **Adzuna** ou **Jooble**.

## 🚀 Fonctionnalités
### Base
- **Recherche d'offres en télétravail** : Affiche les offres disponibles via l'API Remote OK.
- **Filtres dynamiques** : 
  - Recherche par poste.
  - Recherche par compétence (ex. : Python, JavaScript).
- **Tableau interactif** : Visualisation claire des résultats avec possibilité d'exploration.
- **Liens directs vers les offres** : Accédez aux annonces complètes directement depuis l'application.

### Supplément
- **Recherche d'offres sur différents sites** : Ajout de nouvelles API.
- **Ajout d'un filtre** : Ajout d'un filtre de recherche par localisation.
- **Affichage de statistiques** : histogramme des offres par compétence et nuage de mots les plus retrouvés dans les offres.

## 🛠️ Technologies utilisées

- **Python** : Langage principal du projet.
- **Streamlit** : Framework pour créer des applications web interactives.
- **Pandas** : Manipulation et analyse des données.
- **Requests** : Gestion des appels API.

## 📦 Installation

```bash
# Clonez le dépôt
git clone https://github.com/<votre-utilisateur>/job-dashboard.git
cd job-dashboard

# Créez un environnement virtuel (optionnel mais recommandé)
python -m venv env
source env/bin/activate    # Pour Linux/Mac
env\Scripts\activate       # Pour Windows

# Installez les dépendances
pip install -r requirements.txt

# Lancez l'application Streamlit
streamlit run dashboard.py
```

## 📑 Usage
- Lancez l'application localement.
- Accédez au tableau de bord via votre navigateur web (par défaut, http://localhost:8501).
- Utilisez les filtres disponibles dans la barre latérale pour explorer les offres.

## 📋 To-Do
- [ ] Intégration de l'API de Remote OK
- [ ] Filtrage dynamique
- [ ] Amélioration de l'affichage
- [ ] Ajouter une intégration avec d'autres API (Adzuna, Jooble, etc.).
- [ ] Support pour la recherche par localisation.
- [ ] Affichage de statistiques (ex. : histogramme des offres par compétence).

## 🤝 Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le dépôt.
2. Créez une branche avec un nom descriptif : `feature/nouvelle-fonctionnalité`.
3. Soumettez une pull request détaillant les modifications.

## 📜 Licence
Ce projet est sous licence MIT.
