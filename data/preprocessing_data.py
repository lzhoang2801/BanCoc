import pandas as pd
import unicodedata
import os
import re
import warnings
warnings.filterwarnings('ignore')
from underthesea import word_tokenize

patterns = {
	'[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
	'[đ]': 'd',
	'[èéẻẽẹêềếểễệ]': 'e',
	'[ìíỉĩị]': 'i',
	'[òóỏõọôồốổỗộơờớởỡợ]': 'o',
	'[ùúủũụưừứửữự]': 'u',
	'[ỳýỷỹỵ]': 'y'
}

def to_lowercase(sentence):
    return sentence.lower()

def normalize_unicode(sentence):
    return unicodedata.normalize('NFC', sentence)

def remove_accents(sentence):
    for pattern, repl in patterns.items():
        sentence = re.sub(pattern, repl, sentence)
    return sentence

def vietnamese_tokenize(sentence):
    return word_tokenize(sentence, format="text")

def load_data(path):
    if os.path.isfile(path):
        data = pd.read_csv(path)
        data['sentence'] = data['sentence'].apply(to_lowercase).apply(normalize_unicode)
        return data
    else:
        raise FileNotFoundError(f"The file {path} does not exist.")

def load_stopwords(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            stopwords = [normalize_unicode(line.strip().lower()) for line in file.readlines() if line.strip()]
        return list(stopwords)
    else:
        raise FileNotFoundError(f"The file {path} does not exist.")

vietnamese_stopwords = load_stopwords('data/vietnamese-stopwords.txt')
df = load_data('data/intents.csv')

if __name__ == "__main__":
    print("First few rows of the dataset:")
    print(df.head())
    print("")
    print("Information about the dataset:")
    print(df.info())
    print("")
    print("Description of the dataset:")
    print(df.describe())