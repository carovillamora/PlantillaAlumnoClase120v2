# Bibliotecas de preprocesamiento de datos de texto
import nltk
nltk.download("punkt")
nltk.download("wordnet")
import json
import pickle
import numpy as np
import random

ignore_words = ['?', '!',',','.', "'s", "'m"]

# Cargar la biblioteca para el modelo
import tensorflow
from data_preprocessing import get_stem_words

model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Cargar los archivos de datos
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))

def preprocess_user_input(user_input):

    
   
    # Codificación de los datos de entrada
    

def bot_class_prediction(user_input):

    

def bot_response(user_input):

   

# Nota: Las siguientes oraciones se mantienen en inglés para preservar la uniformidad del chatbot
print("Hi I am Stella, How Can I help you?")

while True:
    

