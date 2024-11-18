import os
import json

import google.generativeai as genai

from PIL import Image

working_directory=os.path.dirname(os.path.abspath(__file__))
config_file_path=f"{working_directory}/config.json"

config_data=json.load(open(config_file_path))

Google_api=config_data["Google-api"]

genai.configure(api_key=Google_api)


def load_gemini_ai_model():
    gemini_pro_model=genai.GenerativeModel("gemini-1.5-flash")
    return gemini_pro_model


def gemini_ai_vision(prompt,image):
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    response=gemini_pro_model.generate_content([prompt,image])
    result = response.text
    return result

def Emebbed_Text_Generation(input_text):
    embbeded_model= "models/text-embedding-004"
    emddeding = genai.embed_content(model=embbeded_model,content=input_text,task_type="retrieval_document")
    emddeding_list=emddeding['embedding']
    return emddeding

def gemini_user_response(user_prompt):
    gemini1_pro_model = genai.GenerativeModel("gemini-1.5-flash")

    response1 = gemini1_pro_model.generate_content(user_prompt)

    result = response1.text

    return result
