import json, pickle 
from flask import Flask,render_template, request, jsonify
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np


app = Flask(__name__)

# load data and the model
with open("data/New-data.json")as f:
    data = json.load(f)

model = load_model("models/DL-model.h5")
tokenizer = pickle.load(open(r"models/tokenizer_.pkl","rb"))
le = pickle.load(open(r"models/label-encoder.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods= ["POST"])
def get_response():

    userInput = request.json.get('user_input')
    sequences = tokenizer.texts_to_sequences([userInput])
    padded = pad_sequences(sequences, maxlen =18) 

    result_idx = np.argmax(model.predict(padded))

    final_result =le.inverse_transform([result_idx])[0]

    output= " "
    for label in data["intents"]:
        if label["tag"]==final_result:
               output=np.random.choice(label["responses"])
               break
    
    return jsonify( { 'response':output })

if __name__ == "__main__":
    app.run(debug=True)