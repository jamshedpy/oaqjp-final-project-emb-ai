import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions from the provided text using the Watson Emotion Predict API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: The emotion analysis result.
    """
    myobj = {"raw_document":{"text":text_to_analyze}}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url,json=myobj,headers=header)
    formatted_response = json.loads(response.text)
    return {'text': formatted_response}
   