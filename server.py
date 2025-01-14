"""
Flask server for emotion detection.

This module implements a Flask application to provide
emotion detection as a service using the `emotion_detector` function.
"""

from flask import Flask, jsonify
from emotion_detection import emotion_detector

# Create Flask application
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Endpoint for detecting emotions from text.

    This endpoint takes a hardcoded string, processes it through the
    `emotion_detector` function, and returns a JSON response
    with the emotion scores and the dominant emotion.

    Returns:
        flask.Response: JSON response containing emotion scores and messages.
    """
    # Hardcoded text for analysis
    text_to_analyze = "I love my life"

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Extract the dominant emotion if result is valid
    dominant_emotion = result.get("dominant_emotion")
    if dominant_emotion is None:
        return jsonify({
            "response": "Invalid text! Please try again!",
            "emotions": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        }), 400

    # Format the output as required
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the JSON response
    return jsonify({
        "response": response_message,
        "emotions": result
    }), 200

if __name__ == "__main__":
    app.run(debug=True)

