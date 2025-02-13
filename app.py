import json, pickle
from flask import Flask,render_tempate, request
from tensorflow.keras.preprocessing.sequence import pad_sequeces
from tensorflow.keras.models import load_model

app = Flask(__name__)

# load data and the model
with open("data/pegasus_new_dtaa.json")as f:
    data = json.load(f)

model = load_model("models/DL_model.h5")
tokenizer = pickle.load(open(r"models/tokenizer.pkl","rb"))
le = pickle.load(open(r"models/label_encoder.pkl","rb"))
@ app.route("/")
def home():
    return render_tempate("index.html")

@ app.route("/chat",methods= ["POST"])
def get_response(user_input):
    
