import pandas as pd
import unicodedata
import re
import joblib
from underthesea import word_tokenize
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.filterwarnings('ignore')

INTENT_ENCODING_PATH = 'data/intent_encoding.pkl'

patterns = {
	'[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
	'[đ]': 'd',
	'[èéẻẽẹêềếểễệ]': 'e',
	'[ìíỉĩị]': 'i',
	'[òóỏõọôồốổỗộơờớởỡợ]': 'o',
	'[ùúủũụưừứửữự]': 'u',
	'[ỳýỷỹỵ]': 'y'
}

def to_lowercase(text):
    return text.lower()

def normalize_unicode(text):
    return unicodedata.normalize('NFC', text)

def remove_accents(text):
    for pattern, repl in patterns.items():
        text = re.sub(pattern, repl, text)
    return text

def sentence_preprocessing(text):
    text = to_lowercase(text)
    text = normalize_unicode(text)
    text = remove_accents(text)
    tokens = word_tokenize(text, format="text")
    return ''.join(tokens).strip()

def load_data(path):
    return pd.read_csv(path, sep=';')

def load_stopwords():
    stopwords = pd.read_csv("https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/refs/heads/master/vietnamese-stopwords.txt", sep='\r', header=None)
    return stopwords.values.flatten().tolist()

#vietnamese_stopwords = load_stopwords()
df = load_data('data/intents.csv')

df['sentence'] = df['sentence'].apply(lambda s: sentence_preprocessing(s))
label_encoder = LabelEncoder()
df['intent_encoded'] = label_encoder.fit_transform(df['intent'])

joblib.dump(label_encoder, INTENT_ENCODING_PATH)

if __name__ == "__main__":
    print("First few rows of the dataset:")
    print(df.head())
    print("")
    print("Information about the dataset:")
    print(df.info())
    print("")
    print("Description of the dataset:")
    print(df.describe())
    print("")
    print("Encoded intents:")
    print(df[['intent', 'intent_encoded']].value_counts())