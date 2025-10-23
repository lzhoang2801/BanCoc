import pandas as pd
import unicodedata
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
    data = pd.read_csv(path, sep=';')
    print(data.head())
    data['sentence'] = data['sentence'].apply(to_lowercase).apply(normalize_unicode)
    return data

def load_stopwords():
    stopwords = pd.read_csv("https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/refs/heads/master/vietnamese-stopwords.txt", sep='\r', header=None)
    return stopwords.values.flatten().tolist()

vietnamese_stopwords = load_stopwords()
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