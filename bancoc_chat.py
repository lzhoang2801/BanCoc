import joblib
import numpy as np
from data.preprocessing_data import to_lowercase, normalize_unicode, remove_accents

vectorizer = joblib.load('models/vectorizer.pkl')
lr_model = joblib.load('models/best_model.pkl')

def preprocess_sentence(sentence):
    sentence = to_lowercase(sentence)
    sentence = normalize_unicode(sentence)
    sentence = remove_accents(sentence)
    return sentence

def predict_intent(sentence, confidence_threshold=0.5):
    sentence = preprocess_sentence(sentence)
    sentence = vectorizer.transform([sentence])

    predict = lr_model.predict(sentence)
    probability = lr_model.predict_proba(sentence)
    confidence = np.max(probability)
    
    if confidence > confidence_threshold:
        return {
            "intent": predict,
            "confidence": confidence
        }
    else:
        return {
            "intent": "unknow_intent",
            "predicted_intent": predict,
            "confidence": confidence
        }

def main():
    print("Welcome to Ban Coc Chatbot!")
    while True:
        sentence = input("You: ")
        print(predict_intent(sentence))

if __name__ == "__main__":
    main()