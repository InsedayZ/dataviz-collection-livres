import streamlit as st
import pandas as pd

def analyser_livres(nom_fichier):
    try:
        df = pd.read_csv(nom_fichier)

        st.subheader("Aperçu des données brutes")
        st.dataframe(df)

        st.subheader("1. Répartition des livres par genre")
        genres_counts = df["Genre"].value_counts()
        st.bar_chart(genres_counts)
        st.write("Détail par genre :", genres_counts)

        st.subheader("2. Livres publiés avant 1950")
        livres_anciens = df[df["Annee"] < 1950]
        if not livres_anciens.empty:
            st.dataframe(livres_anciens[["Titre", "Auteur", "Annee"]])
        else:
            st.write("Aucun livre trouvé publié avant 1950.")

    except FileNotFoundError:
        st.error(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

st.title("📚 Analyse de Ma Collection de Livres")
analyser_livres("livres.csv")
