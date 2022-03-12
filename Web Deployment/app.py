import numpy as np
import pandas as pd
import tensorflow as tf

from flask import Flask, request, jsonify, render_template
import pickle
from sklearn import preprocessing
from nltk import word_tokenize,sent_tokenize
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.models import model_from_json
import pickle

app = Flask(__name__, template_folder='templates')

MAX_NB_WORDS = 300000
# Max number of words in each complaint.
MAX_SEQUENCE_LENGTH = 200
# This is fixed.
EMBEDDING_DIM = 100


# with open(r'model files\lsvc.pkl', 'rb') as handle:
#     lsvc = pickle.load(handle)
# lsvc = pickle.load(open(r'model files\lsvc_new.pkl', 'rb'))
import pickle5 as p5
with open(r'model files\lsvc.pkl', "rb") as fh:
    lsvc = p5.load(fh)




json_file = open(r'model files/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights(r'model files\model.h5')


with open(r'model files\tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open(r'model files\label_encoder.pkl', 'rb') as handle:
    label_encoder = pickle.load(handle)   



df = pd.read_csv('2_preprocessed_data.csv')
final_df = df[['preprocessed_text', 'dialect']]
target_encoded = final_df['dialect'].factorize()
labels = target_encoded[1]

le= label_encoder.fit_transform(final_df['dialect'])
final_df['encoded'] = le


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        seq = tokenizer.texts_to_sequences(data)
        padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
        pred_dl = model.predict(padded)
        
        
        prediction_dl = final_df[final_df['encoded'] == int(np.argmax(pred_dl))]['dialect'].values[0]
        # prediction_ml = final_df[final_df['encoded'] == int(np.argmax(pred_ml))]['dialect'].values[0]
        prediction_ml = lsvc.predict(data)[0]
    return render_template('results.html',predict = {'prediction_dl' : prediction_dl, 
                                            'prediction_ml' : prediction_ml})

if __name__ == "__main__":
    app.run(debug=True)