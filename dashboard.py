import streamlit as st
import requests
import pandas as pd
from modules.functions import fetch_jobs
import time
import re

# Configuration de la page Streamlit
st.set_page_config(page_title="Dashboard des Offres d'Emploi", layout="wide")

# Titre de l'application
st.title("🎯 Dashboard des Offres d'Emploi")

strip_cols = ["position", "company", "location"]

# Récupérer les données via l'API
with st.spinner("Chargement des offres d'emploi..."):
    job_data = fetch_jobs()

# Afficher les filtres
with st.sidebar:
    position_input = st.text_input('Poste', '', key='position_filter')
    skills_input = st.text_input('Compétences', '', key='skills_filter')

# Afficher les données si disponibles
if not job_data.empty:
    for col in strip_cols :
        job_data[col] = job_data[col].apply(lambda x: x.strip())

    position_cond = True
    skills_cond = True
    filtered_jobs = job_data
    if position_input != '':
        position_pattern_array = [position_input, position_input.replace('-', ' ')]
        position_pattern = re.compile(f"({'|'.join(position_pattern_array)})", re.IGNORECASE)
        filtered_jobs = job_data.loc[job_data['position'].str.contains(position_pattern, regex=True)]
        
    if skills_input != '':
        skills_pattern_array = skills_input.split(',')
        skills_pattern_array.extend([el.replace('-', ' ') for el in skills_pattern_array if '-' in el])
        skills_pattern_array = [el.strip() for el in skills_pattern_array]
        print(skills_pattern_array)
        # skills_pattern_array = [skills_input, skills_input.replace('-', ' ')]
        skills_pattern = re.compile(f"({'|'.join(skills_pattern_array)})", re.IGNORECASE)
        filtered_jobs = filtered_jobs.loc[filtered_jobs['description'].str.contains(skills_pattern, regex=True)]
    
    # Ajout de liens pour chaque offre
    st.markdown("### 📄 Liste des offres")
    for _, row in filtered_jobs.iterrows():
        print(row['tags'])
        with st.expander(f"#### **{row['position']}** chez **{row['company']}** ({row['location']}) — [Lien vers l'offre]({row['url']})"):
            st.markdown(f"<div style='padding: 2rem;'>{row['description']}</div>", unsafe_allow_html=True)
else:
    st.warning("Aucune offre d'emploi trouvée.")

