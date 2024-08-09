import requests
import json

def emotion_detector(text_to_analyze):
    # URL and headers for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input JSON data
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Sending a POST request to the API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response text to a dictionary
    response_dict = json.loads(response.text)
    # Extract the emotion predictions (first item in the list)
    emotion_predictions = response_dict['emotionPredictions'][0]['emotion']
    # Extract the individual emotion scores
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    # Logic to find the dominant emotion
    emotion_scores = {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    # Returning the formatted result
    return {
        'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 
        'dominant_emotion': dominant_emotion
    }

