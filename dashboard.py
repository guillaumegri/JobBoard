import streamlit as st
import requests
import pandas as pd

# Configuration de la page Streamlit
st.set_page_config(page_title="Dashboard des Offres d'Emploi", layout="wide")

# Titre de l'application
st.title("🎯 Dashboard des Offres d'Emploi en Télétravail")

strip_cols = ["position", "company", "location"]

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

# Récupérer les données via l'API
with st.spinner("Chargement des offres d'emploi..."):
    job_data = fetch_jobs()

# Afficher les données si disponibles
if not job_data.empty:
    for col in strip_cols :
        job_data[col] = job_data[col].apply(lambda x: x.strip())

    # Ajout de liens pour chaque offre
    st.markdown("### 📄 Liste des offres")
    for _, row in job_data.iterrows():
        st.write(f"#### **{row['position']}** chez **{row['company']}** ({row['location']}) — [Lien vers l'offre]({row['url']})")
        st.markdown(f"<div style='padding: 2rem;'>{row['description']}</div>", unsafe_allow_html=True)
else:
    st.warning("Aucune offre d'emploi trouvée.")

