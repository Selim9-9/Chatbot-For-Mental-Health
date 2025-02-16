import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
import json, pickle 

from flask import Flask,render_template, request, jsonify
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
# Load and inspect the model
model = load_model("models/DL_model.h5")
tokenizer = pickle.load(open(r"models/tokenizer.pkl","rb"))
le = pickle.load(open(r"models/label_encoder.pkl","rb"))


app = Flask(__name__)

# load data and the model
with open("data/New-data.json")as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Step 1: Get user input from request
        user_input = request.json.get('user_input')

        # Step 2: Convert input to sequences and pad them
        sent = pad_sequences(tokenizer.texts_to_sequences([user_input]), padding="post", maxlen=18)
        
        # Step 3: Predict class index
        predicted_idx = tf.argmax(model.predict(sent), axis=1)

        # Step 4: Convert predicted index to label (intent)
        predicted_tag = le.inverse_transform(np.array(predicted_idx).reshape(1))[0]

        # Step 5: Get response based on predicted tag
        response = next((np.random.choice(intent["responses"]) for intent in data["intents"] if intent["tag"] == predicted_tag), "Sorry, I didn't understand.")

        # Step 6: Return JSON response (without tag)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({'response': "Connection lost or an error occurred. Please try again."})

if __name__ == "__main__":
    app.run(debug = True)