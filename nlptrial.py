import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
#from nltk.tokenize import sent_tokenize
#from nltk.probability import FreqDist
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')
from nltk.corpus import stopwords
import re
#from sklearn.model_selection import train_test_split
#from sklearn.feature_extraction.text import CountVectorizer

def lemmatize_text(text):
    stop_words = set(stopwords.words("english"))
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lem_list = []
    for w in word_tokenize(text):
        if w not in stop_words:
            lem_list.append(lemmatizer.lemmatize(w))
    return lem_list
def top100(df):
    # Set up
    df["word_tok"] = df.methods.apply(lambda L: re.sub(re.compile('<.*?>'), '', L))
    df.word_tok = df.word_tok.apply(lambda L: re.sub('[^A-Za-z0-9]+', ' ', L))
    df.word_tok = df.word_tok.apply(lambda L: L.lower())
    df.word_tok = df.word_tok.apply(lemmatize_text)
    return df
def main():
    df = pd.read_csv('mockData.csv')
    return top100(df)

if __name__ == "__main__":
    main().to_csv("mockDataLem.csv")