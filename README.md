# PythonForDataAnalysisZaynebALouiseA

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

# Description

"youtube_videos.tsv" contient 10 colonnes de caractéristiques fondamentales de vidéo pour 1,6 million de vidéos youtube; Il contient YouTube:
##### video id, 
##### duration,
##### bitrate(total in Kbits), 
##### bitrate(video bitrate in Kbits), 
##### height(in pixle), -
##### width(in pixles), 
##### framrate, 
##### estimated framerate, 
##### codec, 
##### category,  
##### direct video link. 

Ce dataset peut être utilisé pour obtenir des informations sur les caractéristiques des vidéos grand public trouvées sur UGC (Youtube).

-----------------------------------------------------------------------------------------------------

"transcoding_mesurment.tsv" contient 20 colonnes qui incluent les caractéristiques vidéo d'entrée et de sortie ainsi que leur transcodage les besoins en temps et en ressources de mémoire lors du transcodage de vidéos formats valides. Le deuxième dataset a été collecté sur la base d'expériences sur un Intel CPU i7-3720QM en sélectionnant au hasard deux lignes du premier ensemble de données et en utilisant ceux-ci comme paramètres d'entrée et de sortie d'une application de transcodage vidéo, ffmpeg 4.

##### id = Youtube videp id
##### duration = duration of video
##### bitrate bitrate(video) = video bitrate (quantité de données transmises par seconde)
##### height = height of video in pixles
##### width = width of video in pixles
##### frame rate = actual video frame rate (image à la sec)
##### frame rate(est.) = estimated video frame rate
##### codec = coding standard used for the video
##### category = YouTube video category
##### url = direct link to video (has expiration date)
##### i = number of i frames in the video
##### p = number of p frames in the video
##### b = number of b frames in the video
##### frames = number of frames in video
##### i_size = total size in byte of i videos
##### p_size = total size in byte of p videos
##### b_size = total size in byte of b videos
##### size = total size of video
##### o_codec = output codec used for transcoding
##### o_bitrate = output bitrate used for transcoding
##### o_framerate = output framerate used for transcoding
##### o_width = output width in pixel used for transcoding
##### o_height = output height used in pixel for transcoding
##### umem = total codec allocated memory for transcoding
##### utime = total transcoding time for transcoding

Le deuxième ensemble de données peut être utilisé pour construire une prédiction du temps de transcodage modéliser et montrer l'importance de nos ensembles de données.

# Visualisation

-----------------------------------------------------------------------------------------------------

# Modèles

L'objectif de notre projet est de prédire la target : transcoding time utime.

Le dataset dispose de colonnes string qui poseront problème pour l’exécution du modèle on décide de créer des colonnes pour chaque string qui ressort 0 si il n’y a pas la valeur et 1 sinon. On sépare ensuite le dataset en deux X qui correspond au features et Y la target à prédire. On sépare ensuite le dataset en train et test en 80% / 20%.

Notre problème est un problème de regression car la target à prédire n'a pas de valeurs binaires mais des float. Nous décidons de tester plusieurs modèles:

#### Régression Linéaire
#### Random Forest
#### GridSearch avec Random Forest
#### KNN
#### XGBOOST

Nous choisissons Mean_square_error(MSE) ainsi que l'accuracy R² comme évaluateur pour tous nos modèles. Un MSE parfait vaut 0 et un R² parfait vaut 1.

-----------------------------------------------------------------------------------------------------

## Regression Linéaire

Nous choisissons d'appliquer dans un premier temps un modèle simple de régression, la regression linéaire. 
Les hyper paramètres que nous aurions pu faire varier sont : 
""
fit_interceptbool, default=True
Whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (i.e. data is expected to be centered).

normalizebool, default=False
This parameter is ignored when fit_intercept is set to False. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm. If you wish to standardize, please use StandardScaler before calling fit on an estimator with normalize=False.

copy_Xbool, default=True
If True, X will be copied; else, it may be overwritten.

n_jobsint, default=None
The number of jobs to use for the computation. This will only provide speedup for n_targets > 1 and sufficient large problems. None means 1 unless in a joblib.parallel_backend context. -1 means using all processors. See Glossary for more details.

positivebool, default=False
When set to True, forces the coefficients to be positive. This option is only supported for dense arrays.
""

Cependant, nous n'avons pas jugé nécessaire d'appliquer ces paramètres qui ne nous semblaient pas pertinant dans notre cas.  
## Random forest

Nous appliquons le modèle en faisant varier le nombre d'estimateurs entre 7 valeurs choisis au hasard entre 1 et 650. L'objectif étant de voir l'évolution de la prediction et de trouver une valeur pour laquelle elle est optimal. Nous exécutons RandomForestRegressor sur les valeurs de train, ensuite on fit le modèle et on fait la prédiction sur X_test. On calcul la mean_square_error ainsi que l’accuracy par rapport à Y_test. Dans un premier temps nous lançons ce modèle sans hyper paramètres puis nous le relançons avec des hyper paramètres afin de constater une possible amélioration. 
Temps d'éxucution est moyennement long et la prediction donne une très bonne performance sans hyper paramètres. Or lorsque nous l'éxécutons avec hyper paramètre nous constatons une performance plus faible. Ce modèle est favorable pour un nombre d'estimateurs réduit car il devient très lent lorsque le nombre d'estimateurs dépasse 150. C'est tout de même un bon modèle.

Nous cherchons à determiner les colonnes importantes au modèle afin d’améliorer la prédiction.

Pour pouvoir éxecuter le modèle nous avons dû transformer les colonnes string en booléen. Lors du calcul de l'importance des colonnes toutes ces colonnes booléennes crées ont donc une importance faible. Nous verifions avec la matrice de corélation exécuté dans la partie visualisation et nous avons la confirmation que ces colonnes string sont peu corrélés avec la target, ont choisi donc de ne pas rajouter les colonnes boléennes dans les colonnes importantes. On relance le modèle sur les colonnes qu'on juge importantes.

L'accuracy est plus faibles et MSE plus forte que lorsque nous appliquons le modèle pour les valeurs entières. Etrange
## GridSearch avec random forest

Nous appliquons le modèle GridSearch avec comme estimateur RandomForestRegressor. Nous l'appliquons sur 3 n_estimateurs de random forest différents et ressortons le R² ainsi que MSE. On éxècute le modèle 5 fois afin de voir l'évolution de la prédiction. Le temps d'éxécution est énorme mais valeur de performances intéréssantes car nous obtenons un MSE relativement faible et un R² proche de 1

## KNN

On choisi d’appliquer le modèle K Neighbors aux données. On fait varier le nombre de voisin de 1 à 10. Ici encore nous executons le modèle sans puis avec hyper paramètre afin de constater une évolution. On calcul l’accuracy et la mean_square_error pour chaque essaie. Les valeurs de MSE sont assez élevés et R² assez basses. Le modèle sans hyper paramètre est encore une fois meilleur que celui avec paramètre.Mais il reste moins performant que les précédents modèles.Le temps d'éxécution, lui, est rapide. 

## XGBOOST

Le modèle XGBOOST s'applique de la même manière que random forest. On choisi donc pour estimateurs les mêmes que ceux du random forest afin de pouvoir les comparer plus simplement. Ici aussi nous faisont varier le modèle avec les hyper paramètre. Ce modèle a des performances très proche avec et sans hyper paramètre. Aucun impact des paramètres donc. Le MSE est très élevé et R² est plutôt éloigné de 1. Ce n'est pas le modèle le plus performant bien qu'il soit assez rapide.
