from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import pickle
import json

app = Flask(__name__)

model = load_model(r"D:\PTITHCM\Mon hoc\HK7(2024-2025)\IoT_And_Application\Final\EmailClassifier\models\cnn_spam_classifier.keras")

# Load tokenizer
# tokenizer = Tokenizer(num_words=500)
with open(r"D:\PTITHCM\Mon hoc\HK7(2024-2025)\IoT_And_Application\Final\EmailClassifier\models\tokenizer.pkl", 'rb') as f:
    tokenizer = pickle.load(f)
# Define max sequence length
# max_len = 100
with open(r"D:\PTITHCM\Mon hoc\HK7(2024-2025)\IoT_And_Application\Final\EmailClassifier\models\config.json", 'r') as f:
    config = json.load(f)
max_len = config['max_len']

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.lower().strip()         # Lowercase and trim
    return text

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({'error': 'Message is required'}), 400

        preprocessed_message = preprocess_text(message)

        # Tokenize and pad the input message
        sequences = tokenizer.texts_to_sequences([preprocessed_message])
        padded_sequence = pad_sequences(sequences, maxlen=max_len, padding='post')

        # Predict using the model
        prediction = model.predict(padded_sequence)
        probability = float(prediction[0][0]) * 100  # Convert to percentage
        label_map = {0: 'Spam', 1: 'Not Spam'}
        prediction_label = label_map[int(probability > 50)]  # Threshold at 50%

        return jsonify({
            'message': message,
            'label': prediction_label,
            'probability': probability
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)