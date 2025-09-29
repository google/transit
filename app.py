import streamlit as st
import pandas as pd
import json

st.title("GitHub Explorer")

json_file = st.selectbox("Choisir le fichier", [
    "issues.json", "pulls.json", "issues_comments.json", "pr_comments.json"
])

# Lire le JSON ligne par ligne
data = []
with open(f"github_export/{json_file}", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                obj = json.loads(line)
                data.append(obj)
            except json.JSONDecodeError:
                st.warning(f"Ligne ignorée : {line[:100]} ...")

# Convertir en DataFrame
df = pd.DataFrame(data)

query = st.text_input("Recherche texte")
if query:
    mask = df.astype(str).apply(lambda x: x.str.contains(query, case=False, na=False)).any(axis=1)
    df = df[mask]

st.dataframe(df)
