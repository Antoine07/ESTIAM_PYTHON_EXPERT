# Exercice ETL 

## Objectif

Par équipe de 2 ou 3. Prévoir une soutenance pour la prochaine fois.

:rocket: L'objectif de cet exercice est de pratiquer le processus ETL (Extract, Transform, Load) pour analyser les écarts de salaires des habitants de la ville de Boston par département sur l'année 2018. 

## Instructions

1. **Extraction des données**
   - Créez une fonction `extract_boston_salary` qui prend une URL en entrée et retourne les données de l'API des salaires de Boston. Utilisez la bibliothèque `urllib.request` pour accéder à l'API et `json` pour lire les données.

2. **Transformation des données**
   - Créez une fonction `transform` qui prend les données extraites en entrée et effectue les transformations suivantes :
      - Éliminez les lignes problématiques où la colonne 'TOTAL EARNINGS' est égale à 'TOTAL EARNINGS'.
      - Normalisez le format des données dans la colonne 'TOTAL EARNINGS' en supprimant les virgules et en convertissant le résultat en nombre flottant.

3. **Enregistrement des données**
   - Créez une fonction `save_to_file` qui prend les données transformées en entrée et les enregistre dans un fichier JSON.

4. **Facultatif : Analyse des données agrégées**
   - Créez une fonction `aggregate_department_data` qui prend les données transformées en entrée, ainsi qu'un nom de département en option, et affiche la moyenne des salaires pour ce département.


## Questions sur les générateurs

1. Générateur vs Liste : Expliquez la différence fondamentale entre un générateur et une liste en Python. Dans quelles situations préférez-vous utiliser un générateur plutôt qu'une liste?

1. Avantages des Générateurs : Quels sont les avantages des générateurs par rapport aux structures de données classiques comme les listes lorsqu'il s'agit de traiter de grandes quantités de données?

1. Utilisation de Yield : Quel est le rôle de l'instruction yield dans une fonction génératrice? Comparez son utilisation avec return.

1. Générateur par Lot : Pourquoi utiliser un générateur par lot (batch generator) plutôt qu'un générateur qui traite toutes les données à la fois? Quels sont les avantages en termes de performance et de gestion de la mémoire?

## :pill: Consignes supplémentaires
- N'utilisez pas les bibliothèques `numpy` ou `pandas` pour cet exercice. Utilisez uniquement les modules standard de Python.
- Assurez-vous de commenter votre code pour expliquer chaque étape de votre approche.

## Utilisation des fonctions

Utilisez les fonctions que vous avez créées pour extraire, transformer, et enregistrer les données. Si vous le souhaitez, effectuez également une analyse facultative des données agrégées pour le département **Boston Police Department**.

:rocket: Bon développement ! 