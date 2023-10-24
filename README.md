# Mastodon_Social_Analytics_with_Hadoop_and_HBase

### Script de Collecte de Données (Data_Collection.py)

Le script de collecte de données a pour objectif d'extraire des informations de Mastodon et de les stocker dans un fichier JSON, tout en les enregistrant simultanément dans le système de fichiers distribué Hadoop (HDFS). Voici comment il fonctionne :

- Il se connecte à une instance Mastodon spécifiée à l'aide de la bibliothèque `Mastodon`.
- Il collecte des données à partir de la timeline publique de Mastodon (timeline_public) et les structure en JSON.
- Les données collectées sont sauvegardées dans un fichier nommé `mastodon_data.json`.
- Parallèlement, ces données sont également insérées dans HDFS à l'emplacement préalablement spécifié.

Assurez-vous que votre cluster Hadoop est en cours d'exécution et que vous disposez des autorisations requises pour insérer des données dans HDFS.

## Script MapReduce (Mapreduce.py)

Le script MapReduce, implémenté dans `Mapreduce.py`, est responsable du traitement des données collectées à partir de Mastodon et de l'extraction d'informations précieuses. Voici comment le script fonctionne et ses principales fonctionnalités :

### Aperçu du Script

- **Objectif** : Le script traite les données au format JSON extraites de Mastodon et génère des statistiques significatives.
- **Implémentation** : Il utilise le framework MRJob pour définir les tâches MapReduce.

### Utilisation

Pour exécuter le script MapReduce, suivez ces étapes :

1. Assurez-vous d'avoir Python et MRJob installés.
2. Préparez un fichier JSON contenant les données Mastodon que vous souhaitez traiter.
3. Exécutez le script en spécifiant le fichier JSON en tant qu'entrée.
4. Les résultats du traitement seront stockés dans un fichier de sortie output.txt.
pour exécuter le script :

```bash
python Mapreduce.py mastodon_data.json -o output.txt
```

## HBase Data Storage Script (connection.py)

The `connection.py` script is responsible for storing data from the `output.txt` file into HBase tables. This script uses the HappyBase library to connect to your HBase instance and create tables if they do not already exist. Here's an overview of how the script works:

### Script Overview

- **Purpose**: The script connects to HBase and stores data in two tables, one for user-related information and one for post-related information.
- **Implementation**: It uses the HappyBase library to interact with HBase.

### Usage

To use the script for storing data in HBase, follow these steps:

1. Ensure that you have HappyBase installed and configured to connect to your HBase instance.
2. Make sure you have the `output.txt` file containing the data you want to store.
3. Run the `connection.py` script.

Here's an example command to run the script:

```bash
python connection.py
```

## Apache Airflow DAG (dag.py)

The Apache Airflow DAG, defined in `airflow_dag.py`, automates your data pipeline, ensuring that data is collected, processed, and stored in a coordinated manner. This DAG orchestrates the following tasks:

### DAG Overview

- **Purpose**: The DAG automates the entire data pipeline, from data collection with Mastodon to data processing with MapReduce and data storage in HBase.
- **Implementation**: It uses Apache Airflow's Directed Acyclic Graph (DAG) framework to schedule and execute tasks at specified intervals.

### Usage

To use the Apache Airflow DAG, follow these steps:

1. Ensure that you have Apache Airflow installed and configured to run your DAG.
2. Make sure you have the necessary components and scripts (data collection, MapReduce, HBase connection) in place.
3. Run your Apache Airflow instance, which will trigger the DAG's tasks automatically based on your specified schedule.

Here's an example of running your Apache Airflow DAG:

```bash
airflow trigger_dag task_to_run
```
## Conformité au RGPD

Le Règlement général sur la protection des données (RGPD) est un ensemble de réglementations régissant la protection des données et la vie privée des individus au sein de l'Union européenne (UE). Lorsque vous travaillez avec des données, il est important de comprendre le RGPD et ses implications. Voici comment les considérations du RGPD s'appliquent aux données d'exemple :


### Données d'Exemple et RGPD

1. **ID** : Le champ "id" représente généralement un identifiant unique pour un utilisateur ou une publication. Pour être conforme au RGPD, vous devez vous assurer que ces identifiants n'exposent pas d'informations personnelles sensibles sans le consentement approprié.

2. **Créé le** : "created_at" indique quand le contenu a été créé. Assurez-vous de respecter les politiques de conservation des données du RGPD et de gérer de manière sécurisée les horodatages, en particulier s'ils incluent des données spécifiques à l'utilisateur.

3. **Sensible** : Le champ "sensitive" suggère si le contenu est sensible. Vous devez traiter et protéger les données sensibles avec soin pour respecter la conformité au RGPD.

4. **Texte Spoiler** : Bien que "spoiler_text" ne contienne peut-être pas de données personnelles, il est essentiel d'utiliser un chiffrement approprié et des contrôles d'accès s'il contient des informations sensibles.

5. **Visibilité** : Le champ "visibility" détermine qui peut voir le contenu. Assurez-vous que les contrôles d'accès et les paramètres de confidentialité respectent les exigences du RGPD.

6. **Langue** : "language" est un attribut du contenu. Assurez-vous que le contenu dans différentes langues respecte les réglementations spécifiques de la langue du RGPD, le cas échéant.

7. **URI et URL** : Les URIs et les URL peuvent renvoyer vers des ressources externes. Assurez-vous d'obtenir le consentement approprié et de respecter les politiques de confidentialité du RGPD lors de la diffusion de liens, en tenant compte des implications du RGPD.

8. **Compteur de Réponses, Repartages et Favoris** : Ces mesures ne doivent pas révéler d'informations sensibles spécifiques à l'utilisateur. Mettez en œuvre des mesures de confidentialité appropriées et l'agrégation des données si nécessaire.

9. **Contenu** : Le champ "content" peut contenir du contenu généré par l'utilisateur. Les utilisateurs doivent consentir à la collecte et au stockage de leur contenu conformément aux exigences du RGPD.

10. **Pièces Jointes Multimédias** : Gérez les pièces jointes multimédias de manière à ce qu'elles n'exposent pas d'informations sensibles sur les utilisateurs sans leur consentement approprié.

11. **Mentions et Étiquettes** : Assurez-vous que les mentions et les étiquettes ne révèlent pas de données personnelles sans le consentement de l'utilisateur.

12. **Données du Compte** : "account" inclut des informations de profil d'utilisateur. Traitez et sécurisez correctement ces informations pour respecter la confidentialité du RGPD.

### Conformité et Protection des Données

La conformité au RGPD est une responsabilité complexe, et il est essentiel de mettre en place des pratiques et des politiques de protection des données qui respectent les droits et la vie privée des individus. Recherchez toujours des conseils juridiques lors de la manipulation de données personnelles pour garantir la conformité au RGPD.


