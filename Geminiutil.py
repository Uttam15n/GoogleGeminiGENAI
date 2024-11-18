#Importing the Requried Libraries
import os
import json

import google.generativeai as genai

from PIL import Image

working_directory=os.path.dirname(os.path.abspath(__file__))

config_file_path=f"{working_directory}/config.json"
#opening my google gemini api key file
config_data=json.load(open(config_file_path))
#storing my google gemini api key
Google_api=config_data["Google-api"]

genai.configure(api_key=Google_api)

#creating a function to get text response from google gemini AI
def load_gemini_ai_model():
    gemini_pro_model=genai.GenerativeModel("gemini-1.5-flash")
    return gemini_pro_model

#creating a function to get captions for the give image from google gemini AI
def gemini_ai_vision(prompt,image):
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    response=gemini_pro_model.generate_content([prompt,image])
    result = response.text
    return result

#creating a Function to get Embedded list from google gemini AI
def Emebbed_Text_Generation(input_text):
    embbeded_model= "models/text-embedding-004"
    emddeding = genai.embed_content(model=embbeded_model,content=input_text,task_type="retrieval_document")
    emddeding_list=emddeding['embedding']
    return emddeding

#creating a function to ask question to gemini AI

def gemini_user_response(user_prompt):
    gemini1_pro_model = genai.GenerativeModel("gemini-1.5-flash")

    response1 = gemini1_pro_model.generate_content(user_prompt)

    result = response1.text

    return result
