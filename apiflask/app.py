from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import csv
import pandas as pd
import xgboost 

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    df = pd.DataFrame(data, columns=['duration','width','height','bitrate','framerate','i','p','b','frames','i_size','p_size','size','o_bitrate','o_framerate','o_width','o_height','umem','Codec_flv','Codec_h264','Codec_mpeg4','Codec_vp8','category_Autos & Vehicles','category_Comedy','category_Education','category_Entertainment','category_Film & Animation','category_Gaming','category_Howto & Style','category_Music','category_News & Politics','category_Nonprofits & Activis','category_People & Blogs','category_Pets & Animals','category_Science & Technology','category_Shows','category_Sports','category_Travel & Events','o_Codec_flv','o_Codec_h264','o_Codec_mpeg4','o_Codec_vp8'
])
   # data = np.array(data).reshape((1,-1))
    prediction = np.array2string(model.predict(df))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models/final_prediction_XGBOOST_IMP.pickle'
    model = p.load(open(modelfile,'rb'))  
    app.run(debug=True, host='localhost')
    