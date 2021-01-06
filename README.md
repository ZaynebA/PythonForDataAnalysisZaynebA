# PythonForDataAnalysisZaynebALouiseA


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

"youtube_videos.tsv" contains 10 columns of fundamental 
video characteristics for 1.6 million youtube videos; It contains YouTube 
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

This dataset can be used to gain insight
in characteristics of consumer videos found on UGC(Youtube).

-----------------------------------------------------------------------------------------------------

"transcoding_mesurment.tsv" contains 20 columns
which include input and output video characteristics along with their transcoding 
time and memory resource requirements while transcoding videos to diffrent but 
valid formats. The second dataset was collected based on experiments on an Intel 
i7-3720QM CPU through randomly picking two rows from the first dataset and using 
these as input and output parameters of a video transcoding application, ffmpeg 4 . 

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

the second dataset can be used to build a transcoding time prediction
model and show the significance of our datasets.

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
## Random forest

Nous appliquons le modèle en faisant varier le nombre d'estimateurs entre 7 valeurs choisis au hasard entre 1 et 650. L'objectif étant de voir l'évolution de la prediction et de trouver une valeur pour laquelle elle est optimal. Nous exécutons RandomForestRegressor sur les valeurs de train, ensuite on fit le modèle et on fait la prédiction sur X_test. On calcul la mean_square_error ainsi que l’accuracy par rapport à Y_test.
Temps d'éxucution est moyennement long et la prediction donne une très bonne performance. Ce modèle est favorable pour un nombre d'éstimateurs réduit car il devient très lent lorsque le nombre d'estimateurs dépasse 150. C'est tout de même un bon modèle.

Nous cherchons à determiner les colonnes importantes au modèle afin d’améliorer la prédiction.

Pour pouvoir éxecuter le modèle nous avons dû transformer les colonnes string en booléen. Lors du calcul de l'importance des colonnes toutes ces colonnes booléennes crées ont donc une importance faible. Nous verifions avec la matrice de corélation exécuté dans la partie visualisation et nous avons la confirmation que ces colonnes string sont peu corrélés avec la target, ont choisi donc de ne pas rajouter les colonnes boléennes dans les colonnes importantes. On relance le modèle sur les colonnes qu'on juge importantes.

L'accuracy et MSE sont plus faibles que lorsque nous appliquons le modèle pour les valeurs entières. Etrange
## GridSearch avec random forest

Nous appliquons le modèle GridSearch avec comme estimateur RandomForestRegressor. Nous l'appliquons sur 3 n_estimateurs de random forest différents et ressortons le R² ainsi que MSE. On éxècute le modèle 5 fois afin de voir l'évolution de la prédiction. Le temps d'éxécution est énorme mais valeur de performances intéréssantes car nous obtenons un MSE relativement faible et un R² proche de 1

## KNN

On choisi d’appliquer le modèle K Neighbors aux données. On fait varier le nombre de voisin de 1 à 10. On calcul l’accuracy et la mean_square_error. Les valeurs de MSE sont assez élevés et R² assez basses. Mais le temps d'éxécution est rapide. 

## XGBOOST

Le modèle XGBOOST s'applique de la même manière que random forest. On choisi donc pour estimateurs les mêmes que ceux du random forest afin de pouvoir les comparer plus simplement. Le MSE est très élevé et R² est plutôt éloigné de 1. Ce n'est pas le modèle le plus performant bien qu'il soit assez rapide.
