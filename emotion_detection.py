import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions from the provided text using the Watson Emotion Predict API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: The emotion analysis result in the specified format.
    """
    myobj = {"raw_document": {"text": text_to_analyze}}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Make the API request
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    # print ("dominant_emotion:", {dominant_emotion})
    # Return the result in the specified format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }