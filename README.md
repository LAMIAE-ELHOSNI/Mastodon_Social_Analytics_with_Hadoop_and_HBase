# Mastodon_Social_Analytics_with_Hadoop_and_HBase

### Script de Collecte de Données (Data_Collection.py)

Le script de collecte de données a pour objectif d'extraire des informations de Mastodon et de les stocker dans un fichier JSON, tout en les enregistrant simultanément dans le système de fichiers distribué Hadoop (HDFS). Voici comment il fonctionne :

- Il se connecte à une instance Mastodon spécifiée à l'aide de la bibliothèque `Mastodon`.
- Il collecte des données à partir de la timeline publique de Mastodon (timeline_public) et les structure en JSON.
- Les données collectées sont sauvegardées dans un fichier nommé `mastodon_data.json`.
- Parallèlement, ces données sont également insérées dans HDFS à l'emplacement préalablement spécifié.

Assurez-vous que votre cluster Hadoop est en cours d'exécution et que vous disposez des autorisations requises pour insérer des données dans HDFS.

### Script MapReduce (Mapreduce.py)

Le script MapReduce s'appuie sur le framework MRJob pour effectuer un traitement sur les données collectées depuis Mastodon. Voici son fonctionnement :

- Il utilise MRJob pour définir les différentes étapes MapReduce nécessaires.
- Dans la fonction `mapper`, les données JSON sont analysées pour compter les occurrences des langues des messages.
- La fonction `combiner` consolide les données partielles générées par les mappers.
- La fonction `reducer` agrège les données pour obtenir les statistiques finales.

Pour exécuter le script MapReduce, spécifiez le fichier JSON contenant les données collectées. Les résultats du traitement seront stockés dans un répertoire de sortie.


