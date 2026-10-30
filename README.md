# Projet 1 — Analyse des journaux d'un pare-feu

**Étudiante :** Ndioufa Leye
**Établissement :** ISEP Amadou Trawaré de Diamniadio
**Filière :** Réseaux, Sécurité et Internet des Objets (RSIOT)
**Langage :** Python

## 1. Présentation du projet

Ce projet consiste à analyser les journaux d'un pare-feu d'entreprise afin d'étudier le trafic réseau et de détecter des comportements potentiellement suspects.

L'analyse est réalisée avec Python, Pandas et Matplotlib.

## 2. Objectifs

* Nettoyer les données des journaux réseau.
* Identifier les protocoles et ports les plus utilisés.
* Calculer le pourcentage de connexions refusées.
* Rechercher les adresses IP présentant des comportements suspects.
* Visualiser les résultats avec des graphiques.
* Proposer des recommandations de sécurité.

## 3. Structure du projet

```text
projet-analyse-LEYE-Ndioufa/
│
├── README.md
├── requirements.txt
├── analyse.py
├── rapport.md
├── resultats.json
│
├── data/
│   └── logs_reseau.csv
│
└── figures/
    ├── graphique_actions.png
    ├── graphique_scans.png
    └── graphique_volumes.png
```

## 4. Technologies utilisées

* Python
* Pandas
* Matplotlib
* JSON
* JupyterLab
* Git et GitHub

## 5. Installation et exécution

### Installer les bibliothèques

Dans un terminal ouvert à la racine du projet :

```bash
pip install -r requirements.txt
```

### Exécuter le programme

```bash
python analyse.py
```

Le programme analyse les données et génère automatiquement :

* `resultats.json`
* Les graphiques dans le dossier `figures/`

## 6. Résultats obtenus

| Indicateur                             | Résultat     |
| -------------------------------------- | ------------ |
| Connexions après nettoyage             | 5 440        |
| Port le plus utilisé                   | 443          |
| Connexions refusées                    | 13,57 %      |
| IP suspectée de scan                   | 192.168.1.99 |
| IP avec le volume envoyé le plus élevé | 192.168.1.11 |

### Analyse de sécurité

L'adresse IP `192.168.1.99` a contacté 328 ports différents, ce qui constitue un indice important de scan de ports.

L'adresse IP `192.168.1.11` présente le volume total de données envoyées le plus élevé. Une investigation complémentaire serait nécessaire pour déterminer si ces transferts sont légitimes.

Ces observations ne constituent pas, à elles seules, des preuves d'attaques.

## 7. Visualisations

Les trois graphiques sont disponibles dans le dossier `figures/`.

Ils représentent :

1. La répartition des connexions autorisées et refusées.
2. Les adresses IP ayant contacté le plus de ports distincts.
3. Les adresses IP ayant envoyé le plus de données.

## 8. Rapport

Le fichier `rapport.md` présente les résultats de l'analyse, les comportements suspects et les recommandations de sécurité.

## 9. Conclusion

Ce projet m'a permis de mettre en pratique mes connaissances en Python, analyse de données, réseaux et cybersécurité.

Il montre comment l'analyse des journaux d'un pare-feu peut contribuer à la détection d'activités réseau inhabituelles.
