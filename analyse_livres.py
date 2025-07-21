import streamlit as st
import pandas as pd

def analyser_livres(nom_fichier):
    try:
        # Lire le fichier CSV avec pandas
        df = pd.read_csv(nom_fichier)

        # Afficher les premières lignes du DataFrame pour vérification
        st.subheader("Aperçu des données brutes")
        st.dataframe(df)

        # 1. Répartition par genre
        st.subheader("1. Répartition des livres par genre")
        genres_counts = df["Genre"].value_counts()
        st.bar_chart(genres_counts)
        st.write("Détail par genre:", genres_counts)

        # 2. Livres publiés avant 1950
        st.subheader("2. Livres publiés avant 1950")
        livres_anciens = df[df["Annee"] < 1950]
        if not livres_anciens.empty:
            st.dataframe(livres_anciens[["Titre", "Auteur", "Annee"]])
        else:
            st.write("Aucun livre trouvé publié avant 1950.")

    except FileNotFoundError:
        st.error(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé. Assurez-vous qu'il est dans le même dossier que le script.")
    except Exception as e:
        st.error(f"Une erreur est survenue lors de l'analyse : {e}")

# Titre de l'application Streamlit
st.title("Analyse de Ma Collection de Livres")

# Appel de la fonction d'analyse avec le nom du fichier CSV
analyser_livres("livres.csv")

