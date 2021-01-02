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
