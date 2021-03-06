# PythonForDataAnalysisZaynebALouiseA

# Objectif de l'artcile asscocié à notre dataset 'VIDEO TRANSCODING TIME PREDICTION FOR PROACTIVE LOAD BALANCING'

Le dataset que nous avons : https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset a été utilisé dans le cadre de recherches. Ces chercheurs ont écrit un artcile ***'Video transcoding time prediction for proactive load balancing'*** .L'objectif de cet article est présenté dans son abstract que nous avons traduit en francais :

"Dans cet article, nous présentons une méthode permettant de prédire le temps de transcodage des vidéos en fonction d'un flux vidéo d'entrée et de ses paramètres de transcodage. Le temps de transcodage des vidéos est traité comme une variable aléatoire et est statistiquement prédit à partir d'observations passées. La méthode que nous proposons prédit le temps de transcodage en fonction de plusieurs paramètres des flux vidéo d'entrée et de sortie, et ne nécessite aucune information détaillée sur le codec utilisé. Nous démontrons l'efficacité de notre méthode en comparant les prédictions résultantes avec les temps de transcodage réels sur des flux vidéo non vus. Les résultats de la simulation montrent que notre méthode de prédiction permet un équilibrage de charge des travaux de transcodage nettement meilleur que les méthodes classiques d'équilibrage de charge."

D'après cet abstract, l'objectif premier est de présenter une méthode qui permet de prédire le temps de transcodage des vidéos en fonction d'un flux vidéo d'entrée et de ses paramètres de transcodage. Cette méthode est ensuite testée sur des flux de vidéo non vus.

Dans notre étude, nous allons donc nous pencher sur la prédiction du temps de transcodage d'une vidéo en fonction, entre autre, de ses paramètres de transcodage. Nous testerons ensuite nos modèles sur un test set. Puis nous comparerons nos modèles pour trouver la meilleure solution.

# Introduction au sujet 
Ce que l'on appelle abusivement un fichier vidéo est avant tout un conteneur. Le concept est simple, il entrelace en son sein les différents contenus du fichier, à savoir la piste vidéo, la piste audio, et éventuellement les pistes de sous titre.

#### Transcodage
Lorsque l'on parle de solutions de transcodage, on parle donc de changer un ou plusieurs des formats présents dans le fichier original. On peut changer les formats de compression pour obtenir un fichier plus petit. Par exemple convertir un DVD (conteneur VOB, vidéo MPEG-2, audio Dolby Digital) en un fichier vidéo (AVI, XviD, MP3). Parfois on peut souhaiter garder un même format vidéo mais réduire la taille des fichiers, par exemple en convertissant un Blu-ray (.m2ts, H.264, DTS-HD) en un fichier lisible sur une tablette (.mp4, H.264, AAC) ou une console de jeux. Même si l'on ne change pas de format vidéo (H.264 de chaque côté), on peut souhaiter recompresser la vidéo, soit pour des questions de taille de fichier (les Blu-ray sont volumineux), de taille d'écran destination (réduire à 1280 par 720 au lieu de 1920 par 1080) ou de spécificité de la machine destination (un iPad par exemple ne peux pas lire tous les « niveaux » de compression H.264, d'où la notion de profil existante à l'intérieur de la norme, voir page suivante).

# Enoncé
1. Un powerpoint expliquant les tenants et aboutissant du problème, vos réflexions sur la
question posée, les différentes variables que vous avez créées, comment se situe le
problème dans le contexte de l’étude, etc : 25 %
2. Un code en python :
a. Data-visualisation (utilisez matplotlib, searborn, bokeh…) – montrez le lien
entre les variables et la cible : 25%
b. Modélisation – prenez scikit-learnn essayez plusieurs algorithmes, changez les
hyper paramètres, faites une grille de recherche, comparez les résultats de vos
modèles dans des graphiques : 25%
3. Transformation du modèle en API Django : 25%

# Description du dataset

"youtube_videos.tsv" contient 10 colonnes de caractéristiques fondamentales de vidéo pour 1,6 million de vidéos youtube; Il contient YouTube:
* video id, 
* duration,
* bitrate(total in Kbits), 
* bitrate(video bitrate in Kbits), 
* height(in pixle), -
* width(in pixles), 
* framrate, 
* estimated framerate, 
* codec, 
* category,  
* direct video link. 

Ce dataset peut être utilisé pour obtenir des informations sur les caractéristiques des vidéos grand public trouvées sur UGC (Youtube).

-----------------------------------------------------------------------------------------------------

"transcoding_mesurment.tsv" contient 20 colonnes qui incluent les caractéristiques vidéo d'entrée et de sortie ainsi que leur transcodage les besoins en temps et en ressources de mémoire lors du transcodage de vidéos formats valides. Le deuxième dataset a été collecté sur la base d'expériences sur un Intel CPU i7-3720QM en sélectionnant au hasard deux lignes du premier ensemble de données et en utilisant ceux-ci comme paramètres d'entrée et de sortie d'une application de transcodage vidéo, ffmpeg 4.
Pour résumé, le second datset reprend 1099 vidéos du premier dataset. Des test de transcodage on été appliqué à ces vidéos. Ce sont les résultas de ces tests qui sont dans ce dataset.

* id = Youtube videp id
* duration = duration of video
* bitrate bitrate(video) = video bitrate (quantité de données transmises par seconde)
* height = height of video in pixles
* width = width of video in pixles
* frame rate = actual video frame rate (image à la sec)
* frame rate(est.) = estimated video frame rate
* codec = coding standard used for the video
* category = YouTube video category
* url = direct link to video (has expiration date)
* i = number of i frames in the video
* p = number of p frames in the video
* b = number of b frames in the video
* frames = number of frames in video
* i_size = total size in byte of i videos
* p_size = total size in byte of p videos
* b_size = total size in byte of b videos
* size = total size of video
* o_codec = output codec used for transcoding
* o_bitrate = output bitrate used for transcoding
* o_framerate = output framerate used for transcoding
* o_width = output width in pixel used for transcoding
* o_height = output height used in pixel for transcoding
* umem = total codec allocated memory for transcoding
* utime = total transcoding time for transcoding

Le deuxième ensemble de données peut être utilisé pour construire une prédiction du temps de transcodage modéliser et montrer l'importance de nos ensembles de données.

-----------------------------------------------------------------------------------------------------

# Visualisation

Dans cette partie visualisation nous avons d'abord visualisé les NA pour en conclure qu'il n'y en avait pas.

Dans un second temps, nous avons fait des observations génarales sur les vidéos Youtube du dataset "youtube_videos.tsv", comme par exemple le top des catégroies les plus regardées.

Ensuite, nous avons fusionné les 2 dataset "youtube_videos.tsv" et "transcoding_mesurment.tsv" pour avoir un dataset avec des informations complètes sur un échantillon de ces vidéos. Plusieurs tests de transcodage ont été fait sur ces vidéos. 

Enfin, nous avons fait des observation sur ce dataset fusionné pour avoir des informations sur les transcadages des vidéos Youtube. Nous avons entre - autre repérer les colonnes qui nous semblaient corrélées avec la target Utime. (plus d'informations dans le PowerPoint)


-----------------------------------------------------------------------------------------------------

# Modèles

L'objectif de notre projet est de prédire la target : transcoding time 'Utime'.

Le dataset dispose de colonnes string qui poseront problème pour l’exécution du modèle on décide de créer des colonnes pour chaque string qui ressort 0 si il n’y a pas la valeur et 1 sinon (one-hot encoding). On sépare ensuite le dataset en deux X qui correspond au features et Y la target à prédire. On sépare ensuite le dataset en train et test en 80% / 20%.

Notre problème est un problème de regression car la target à prédire n'a pas de valeurs binaires mais des float. Nous décidons de tester plusieurs modèles:

#### Régression Linéaire
#### Random Forest
#### GridSearch avec Random Forest
#### KNN
#### XGBOOST

Nous choisissons Mean_square_error(MSE) ainsi que l'accuracy R² comme évaluateurs pour tous nos modèles. Un MSE parfait vaut 0 et un R² parfait vaut 1.

-----------------------------------------------------------------------------------------------------

## Regression Linéaire

Nous choisissons d'appliquer dans un premier temps un modèle simple de régression, la regression linéaire. 

## Random forest

Nous appliquons le modèle en faisant varier le nombre d'estimateurs entre 7 valeurs choisis au hasard entre 1 et 650. L'objectif étant de voir l'évolution de la prediction et de trouver une valeur pour laquelle elle est optimal. Nous exécutons RandomForestRegressor sur les valeurs de train, ensuite on fit le modèle et on fait la prédiction sur X_test. On calcul la mean_square_error ainsi que l’accuracy par rapport à Y_test. Dans un premier temps nous lançons ce modèle sans hyper paramètres puis nous le relançons avec des hyper paramètres afin de constater une possible amélioration. 

Temps d'éxucution est moyennement long et la prediction donne une très bonne performance sans hyper paramètres (meilleur resultats: R2=0.999986 et MSE=0.061915).

Nous cherchons à voir si nous pouvons encore plus perfectionner le modèle de base en jouant avec les hyperparamètres.

Lorsque nous l'éxécutons avec hyper paramètre nous constatons une performance plus faible. Ce modèle est favorable pour un nombre d'estimateurs réduit car il devient très lent lorsque le nombre d'estimateurs dépasse 150. C'est tout de même un bon modèle.

L'étape suivante était de regarder l'importance des colonnes afin de voir si celles-ci ont un impact dans la prédiction.
Pour pouvoir éxecuter le modèle nous avons dû transformer les colonnes string en booléen (one hot encoding). Lors du calcul de l'importance des colonnes toutes ces colonnes booléennes crées ont donc une importance faible.
Or d'après les visualisation de la partie précedente, 'o_coedc' pourrait avoir une certaine influence sur le temps de transcodage.
Nous décidons quand même d'enlever cette feature ainsi que les autres features 'string' de base pour voir si le modèle a des résultas qui varient.
On remarque que les valeurs d 'évaluations sont moins bonnes que le modèle de base . On peut en déduire que les feature comme o_coedc jouent un rôle dans la précision du modèle. On décide donc de garder toutes les features dans les modèles suivants.

## GridSearch avec random forest

Nous appliquons l'algorithme GridSearch avec RandomForestRegressor. Nous l'appliquons sur 3 n_estimateurs différents et ressortons le R² ainsi que MSE.
On veut voir avec cette grille de rechercher différents paramètres possibles pour le modèle Random Forest et voir ce que l'algorihme trouve comme meilleur solution. Le temps d'éxécution est énorme mais valeur de performances intéréssantes car nous obtenons un MSE relativement faible et un R² proche de 1.

## KNN

On choisi d’appliquer le modèle K Neighbors aux données. On fait varier le nombre de voisin de 1 à 10. Ici encore nous executons le modèle sans puis avec hyper paramètre afin de constater une évolution. On calcul l’accuracy R2 et la mean_square_error pour chaque essaie. Les valeurs de MSE sont assez élevés par rapport à celui du random forest.Le R² a une valeur objectivement haute (max : 0.92) , mais moins que celle du Random Forest. 
Ensuite en y ajoutant des hyperparamètres (ici leaf_size=30,n_jobs=-1), nous constatons une baisse des performances lorsque l'on regarde le R2 et le MSE. On en conlue que le KNN simple est une meilleur solution.
Mais ce modèle reste moins performant que les précédents modèles.Le temps d'éxécution, lui, est rapide. 

## XGBOOST

Le modèle XGBOOST s'applique de la même manière que random forest. On choisi donc pour estimateurs les mêmes que ceux du random forest afin de pouvoir les comparer plus simplement. Ici aussi nous faisont varier le modèle avec les hyper paramètres (ici gamma=10). Ce modèle a des performances très proche avec et sans hyper paramètre même si on remarque qu'il est très légèrement meilleur avec.

# Comparaison des modèles 



![137244482_433291444463529_5182809428197153166_n](https://user-images.githubusercontent.com/57664959/104026948-f8887900-51c6-11eb-92df-880d1493f263.png)

![136423356_461424774853521_7408076743741854134_n](https://user-images.githubusercontent.com/57664959/104026917-ec9cb700-51c6-11eb-86f6-a8868ad7afe4.png)



# Conclusion des modèles 
Pour conclure cette partie, on peut remarquer que les modèles testés ont en général plutôt bien, voir très bien fonctionné dans la prédiction de la feature Utime.

Les meilleurs modèles pour cette prédiction de la feature Utime, avec les MSE les plus bas et les R2 les plus haut sont : Le Random Forest de base (RF) , et le XGBoost  (XGBoost_IMP ).

Ces très bon résultas peuvent sûrement s'expliquer du fait que l'une des variables qui a participé à la prédiction est la variable Umem qui correspond à la mémoire allouée pour le transcodage. En effet il est logique que plus la mémoire utilisée est grande, plus le temps de transcodage sera long. Pour appuyer cette observation, on voit dans la matrice de confusion que Umem est fortement corrélée à utime.
De plus,généralement lorsque l'on veut prédire un temps de transcodage , la mémoire allouée pour ce transcodage n'est pas connu.En effet, dans l'article scientifique, les auteurs ont construit leur modèle en prenant des paramètres en entrée. Ces paramètres incluaient : bitrate, framerate, resolution, codec, number of i frames,
number of p frames, number of b frames, size of i frames, size of p
frames and size of b frames de le vidéo d'entrée et le bitrate, framerate, resolution and codec désiré de la vidéo sortante. Umem n'est donc pas dans cette liste.  De ce fait, si nous avions eu plus de temps, nous aurions pu tester de nouveau les modèles en retirant la feature Umem en entrée.

Pour finir on peut voir que l'ajout d'hyperparamètres aux modèles ne donne pas forcément de meilleurs résultas. De plus, les modèles Random Forest et XGBoost donnent des résultats aussi bon l'un que l'autre, alors que le modèle XGBoost est un modèle beaucou plus puissant. Ces obeservations peuvent peut-etre s'expliquer par le fait que la prédiction de Utime est un problème simple, accentué par le fait que nous possédons la feature Umem en entrée, comme éxpliqué plus haut.

# API 

Pour l'APi nous avons choisi de la coder en python + Flask.
Nous avons crée 2 fichiers : app.py et request.py.

Le modèle que nous avons choisi de tester avec l'API est le XGBoost car c'est l'un des deux modèles qui fonctionnait le mieux pour notre problème de prédiction.

L'API que nous avons faite se compose de 2 fichiers.

L'**app.py**qui sert à charger le modèle enregistré sous format pickle (dans le dossier models) et exécuter celui-ci sur le petite jeu de données test choisi.
Pour se faire nous avons inséré 5 lignes du X_test de notre dataset dans un tableau puis nous avons transformé ce tableau en Dataframe avant de les passer en entré du modèle.

Le fichier **request.py** nous sert à tester l'Api avec un modèle. C'est dans ce fichier que nous insérons les données à tester pour ensuite les passer à l'app.py. Les données à tester ont été tiré du X_train du dataset. Nous y avons pris 5 lignes de manière aléàtoire et les avons mis dans un tableau.

Pour lancer l'API nous devons ouvrir 2 terminals : 1 pour lancer l'app.py et le 2ème pour avoir les résultats de prédiction du modèle request.py.

Voici un exemple des résultas que nous obtenons en lancant les 2 terminals sur le jeu de données des 5 lignes de test :

![app](https://user-images.githubusercontent.com/71490248/104068483-4ae88a80-5205-11eb-9751-3e4e8c4ac71b.JPG)

![requetst](https://user-images.githubusercontent.com/71490248/104068241-dc0b3180-5204-11eb-8e96-a2329291725b.JPG)


