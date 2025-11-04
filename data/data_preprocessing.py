import pandas as pd
import unicodedata
import re
from underthesea import word_tokenize

import warnings
warnings.filterwarnings('ignore')

patterns = {
	'[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
	'[đ]': 'd',
	'[èéẻẽẹêềếểễệ]': 'e',
	'[ìíỉĩị]': 'i',
	'[òóỏõọôồốổỗộơờớởỡợ]': 'o',
	'[ùúủũụưừứửữự]': 'u',
	'[ỳýỷỹỵ]': 'y'
}

def load_stopwords():
    stopwords = pd.read_csv("https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/refs/heads/master/vietnamese-stopwords.txt", sep='\r', header=None)
    return stopwords.values.flatten().tolist()

stopwords = load_stopwords()

def normalize_unicode(text):
    return unicodedata.normalize('NFC', text)

def remove_accents(text):
    for pattern, repl in patterns.items():
        text = re.sub(pattern, repl, text)
    return text

def text_cleaning(text):
    text = text.lower()
    text = normalize_unicode(text)
    text = remove_accents(text)
    tokens = word_tokenize(text, format="text")
    return ''.join(tokens).strip()

def load_data(path):
    return pd.read_csv(path, sep=';')