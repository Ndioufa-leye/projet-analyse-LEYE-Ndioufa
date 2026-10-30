
# Importer la bibliothèque permettant de gérer les dossiers
from pathlib import Path

# Créer automatiquement le dossier figures s'il n'existe pas
Path("figures").mkdir(exist_ok=True)

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

print("Bibliothèques importées avec succès !")


# In[2]:


df = pd.read_csv("data/logs_reseau.csv")

df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


# Nombre de lignes avant nettoyage
print("Avant nettoyage :", len(df))

# Supprimer les doublons exacts
df = df.drop_duplicates()

# Nombre de lignes après suppression
print("Après suppression :", len(df))


# In[6]:


# Uniformiser les protocoles
df["protocol"] = df["protocol"].str.upper()

# Vérifier les protocoles
print(df["protocol"].unique())


# In[7]:


# Calculer la médiane
mediane = df["bytes_sent"].median()

# Remplacer les valeurs manquantes
df["bytes_sent"] = df["bytes_sent"].fillna(mediane)

# Vérifier
print("Médiane :", mediane)
print("Valeurs manquantes restantes :", df["bytes_sent"].isnull().sum())


# In[8]:


print("Nombre de lignes :", len(df))
print("Doublons restants :", df.duplicated().sum())
print("Valeurs manquantes :")
print(df.isnull().sum())


# In[9]:


print(df.columns.tolist())


# In[10]:


print("=== PROTOCOLES LES PLUS UTILISÉS ===")

print(df["protocol"].value_counts())


# In[11]:


print("=== VÉRIFICATION ===")

print("Nombre de lignes :", len(df))
print("Doublons :", df.duplicated().sum())
print("Valeurs manquantes dans bytes_sent :",
      df["bytes_sent"].isnull().sum())


# In[12]:


# Afficher le titre de notre analyse
print("=== TOP 10 DES PORTS UTILISÉS ===")

# Sélectionner la colonne des ports de destination
# Compter le nombre de connexions pour chaque port
# Garder uniquement les 10 ports les plus utilisés
top_ports = df["dst_port"].value_counts().head(10)

# Afficher les résultats
print(top_ports)


# In[18]:


# Afficher les différentes actions du pare-feu
print("=== ACTIONS DU PARE-FEU ===")

# Compter les connexions pour chaque action
print(df["action"].value_counts())

# Mettre les actions en majuscules pour faciliter la comparaison
actions = df["action"].str.strip().str.upper()

# Compter les connexions bloquées
nb_bloquees = (actions == "DENY").sum()

# Calculer le pourcentage des connexions bloquées
pourcentage = (nb_bloquees / len(df)) * 100

# Afficher les résultats
print("Connexions bloquées :", nb_bloquees)
print("Pourcentage :", round(pourcentage, 2), "%")


# In[14]:


# Afficher le titre de l'analyse
print("=== TOP 10 DES ADRESSES IP SOURCES ===")

# Sélectionner la colonne des adresses IP sources
# Compter le nombre de connexions générées par chaque adresse IP
# Garder les 10 adresses IP les plus actives
top_ip = df["src_ip"].value_counts().head(10)

# Afficher les résultats
print(top_ip)


# In[15]:


# Afficher les différentes actions enregistrées par le pare-feu
print("=== ACTIONS DU PARE-FEU ===")

# Compter le nombre d'occurrences de chaque action
print(df["action"].value_counts(dropna=False))


# In[16]:


# Afficher le titre de notre analyse
print("=== ANALYSE DE L'IP 192.168.1.99 ===")

# Sélectionner uniquement les connexions provenant de cette adresse IP
ip_suspecte = df[df["src_ip"] == "192.168.1.99"]

# Afficher le nombre total de connexions
print("Nombre de connexions :", len(ip_suspecte))

# Compter le nombre de ports de destination différents
print("Nombre de ports différents :", ip_suspecte["dst_port"].nunique())

# Afficher les ports les plus sollicités
print("\nPorts les plus utilisés :")
print(ip_suspecte["dst_port"].value_counts().head(10))

# Afficher les actions du pare-feu pour cette IP
print("\nActions du pare-feu :")
print(ip_suspecte["action"].value_counts())


# In[17]:


# Afficher le titre
print("=== DÉTECTION DES SCANS DE PORTS ===")

# Regrouper les connexions par adresse IP source
# Compter les ports de destination différents pour chaque IP
scans = df.groupby("src_ip")["dst_port"].nunique()

# Trier les résultats du plus grand au plus petit
scans = scans.sort_values(ascending=False)

# Afficher les 10 adresses IP qui contactent le plus de ports différents
print(scans.head(10))


# In[19]:


# Importer la bibliothèque de visualisation
import matplotlib.pyplot as plt

# Compter le nombre de connexions pour chaque action
actions_counts = df["action"].value_counts()

# Définir la taille du graphique
plt.figure(figsize=(8, 5))

# Créer un graphique en barres
plt.bar(
    actions_counts.index,
    actions_counts.values,
    color=["green", "red"]
)

# Ajouter un titre
plt.title("Répartition des actions du pare-feu")

# Nommer les axes
plt.xlabel("Actions du pare-feu")
plt.ylabel("Nombre de connexions")

# Afficher une grille horizontale
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Ajuster la présentation
plt.tight_layout()

# Enregistrer le graphique
plt.savefig("graphique_actions.png")

# Afficher le graphique
plt.show()


# In[20]:


# Importer la bibliothèque Matplotlib
import matplotlib.pyplot as plt

# Regrouper les connexions par adresse IP source
# Compter le nombre de ports différents contactés par chaque IP
ports_par_ip = df.groupby("src_ip")["dst_port"].nunique()

# Trier les résultats du plus grand au plus petit
ports_par_ip = ports_par_ip.sort_values(ascending=False)

# Sélectionner les 10 premières adresses IP
top_10 = ports_par_ip.head(10)

# Définir la taille du graphique
plt.figure(figsize=(10, 6))

# Créer un graphique en barres horizontales
plt.barh(top_10.index, top_10.values, color="orange")

# Ajouter un titre
plt.title("Top 10 des IP selon le nombre de ports contactés")

# Nommer les axes
plt.xlabel("Nombre de ports différents")
plt.ylabel("Adresses IP sources")

# Placer l'IP la plus active en haut
plt.gca().invert_yaxis()

# Ajouter une grille verticale
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Ajuster la présentation
plt.tight_layout()

# Enregistrer le graphique
plt.savefig("graphique_scans.png")

# Afficher le graphique
plt.show()


# In[21]:


# Afficher le titre de notre analyse
print("=== TOP 10 DES TRANSFERTS DE DONNÉES ===")

# Trier les connexions selon la quantité de données envoyées
# ascending=False permet de classer du plus grand au plus petit
top_transferts = df.sort_values(
    by="bytes_sent",
    ascending=False
)

# Sélectionner les 10 connexions avec les plus gros transferts
top_transferts = top_transferts.head(10)

# Afficher les informations importantes de ces connexions
print(
    top_transferts[
        ["src_ip", "dst_ip", "dst_port", "bytes_sent", "action"]
    ]
)


# In[22]:


# Afficher le titre
print("=== VOLUME DE DONNÉES PAR IP SOURCE ===")

# Regrouper les connexions par adresse IP source
# Additionner les octets envoyés par chaque adresse IP
volume_par_ip = df.groupby("src_ip")["bytes_sent"].sum()

# Trier les résultats du plus grand au plus petit
volume_par_ip = volume_par_ip.sort_values(ascending=False)

# Sélectionner les 10 adresses IP ayant envoyé le plus de données
top_volume = volume_par_ip.head(10)

# Afficher les résultats
print(top_volume)


# In[23]:


# Importer la bibliothèque de visualisation
import matplotlib.pyplot as plt

# Définir la taille du graphique
plt.figure(figsize=(11, 6))

# Créer un graphique en barres horizontales
# Chaque barre représente le volume envoyé par une adresse IP
plt.barh(
    top_volume.index,
    top_volume.values,
    color="royalblue"
)

# Ajouter un titre au graphique
plt.title("Top 10 des adresses IP selon le volume de données envoyées")

# Nommer les axes
plt.xlabel("Volume de données envoyées (octets)")
plt.ylabel("Adresses IP sources")

# Afficher l'adresse IP ayant envoyé le plus de données en haut
plt.gca().invert_yaxis()

# Ajouter une grille verticale
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Améliorer la présentation
plt.tight_layout()

# Enregistrer notre troisième graphique
plt.savefig("graphique_volumes.png")

# Afficher le graphique dans JupyterLab
plt.show()


# In[24]:


# Importer la bibliothèque permettant de créer des fichiers JSON
import json

# Calculer le nombre total de connexions
total_connexions = len(df)

# Compter les connexions refusées par le pare-feu
nb_bloquees = (
    df["action"].str.strip().str.upper() == "DENY"
).sum()

# Calculer le pourcentage de connexions refusées
pourcentage_bloque = (nb_bloquees / total_connexions) * 100

# Identifier le port de destination le plus utilisé
port_frequent = df["dst_port"].value_counts().idxmax()

# Identifier l'adresse IP ayant contacté le plus de ports différents
ip_scan = scans.idxmax()

# Compter les ports différents contactés par cette adresse IP
nombre_ports = scans.max()

# Identifier l'adresse IP ayant envoyé le plus grand volume de données
ip_volume = volume_par_ip.idxmax()

# Récupérer le volume total envoyé par cette adresse IP
volume_max = volume_par_ip.max()

# Afficher un message de confirmation
print("Les résultats sont prêts !")


# In[25]:


# =====================================================
# CRÉATION DES RÉSULTATS AU FORMAT JSON
# =====================================================

# Créer un dictionnaire contenant les cinq résultats
# demandés par le professeur

resultats = {

    # Nombre de lignes après nettoyage
    "nb_lignes_apres_nettoyage": int(len(df)),

    # Port de destination le plus utilisé
    "top_port": int(port_frequent),

    # Pourcentage de connexions refusées
    "taux_deny_pct": round(float(pourcentage_bloque), 2),

    # Adresse IP ayant contacté le plus de ports différents
    "ip_scanner": str(ip_scan),

    # Adresse IP ayant envoyé le plus grand volume de données
    "ip_exfiltration": str(ip_volume)
}

# Afficher les résultats pour vérification
print(resultats)


# In[26]:


# Ouvrir ou créer le fichier resultats.json
# Le mode "w" permet d'écrire dans le fichier
# encoding="utf-8" permet de gérer les caractères accentués
with open("resultats.json", "w", encoding="utf-8") as fichier:

    # Enregistrer les résultats au format JSON
    json.dump(
        resultats,
        fichier,
        indent=4,
        ensure_ascii=False
    )

# Afficher un message de confirmation
print("Fichier resultats.json créé avec succès !")


# In[ ]:




