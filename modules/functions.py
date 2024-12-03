import requests
import pandas as pd
import streamlit as st
def fix_encoding(text, int_encoding = "latin1"):
    try:
        # Tente de corriger avec remplacement des caractères invalides
        fixed_text = text.encode(int_encoding, errors='replace').decode('utf-8', errors='replace')
    except Exception:
        fixed_text = text

    return fixed_text

# Fonction pour appeler l'API Remote OK
@st.cache_data  # Mise en cache pour éviter des appels répétés
def fetch_jobs():
    url = "https://remoteok.com/api"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Convertir en DataFrame et filtrer les colonnes utiles
        jobs = pd.DataFrame(data[1:])  # On saute le premier élément (métadonnées)
        jobs = jobs.map(lambda x: fix_encoding(x) if isinstance(x, str) and not x == '' else x)
        
        return jobs[["position", "company", "location", "description", "tags", "url"]]
    else:
        st.error("Erreur lors de la récupération des données.")
        return pd.DataFrame()