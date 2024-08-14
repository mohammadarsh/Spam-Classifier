# download_nltk_data.py
import nltk

def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

if __name__ == "__main__":
    download_nltk_data()
