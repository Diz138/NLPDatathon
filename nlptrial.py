import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
#from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')
from nltk.corpus import stopwords
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def lemmatize_text(text):
    stop_words = stopwords.words("english")
    new_stopwords = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","et","al"]
    stop_words.extend(new_stopwords)
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lem_list = []
    for w in word_tokenize(text):
        if w not in stop_words:
            lem_list.append(lemmatizer.lemmatize(w))

    tagged = nltk.pos_tag(lem_list)
    noun_adj_tagged = [(word, tag) for word, tag in tagged
                       if tag.startswith('NN') or tag.startswith('NNPS') or tag.startswith('NNP') or tag.startswith(
            'NNS')]
    return noun_adj_tagged
    #return lem_list



def top100(df):
    # Set up
    df["word_tok"] = df.article.apply(lambda L: re.sub(re.compile('<.*?>'), '', L))
    df.word_tok = df.word_tok.apply(lambda L: re.sub('[^A-Za-z]+', ' ', L))
    df.word_tok = df.word_tok.apply(lambda L: L.lower())
    df.word_tok = df.word_tok.apply(lemmatize_text)
    freq_test = []
    for i in range(df.shape[0]):
        freq_test = freq_test + df.word_tok[i]
    filtered_words = []
    for word in freq_test:
        filtered_words.append(word)
    fdist = FreqDist(filtered_words)

    return fdist.most_common(100), df, filtered_words
def main():
    #df = pd.read_csv('mockData.csv')
    df = pd.read_json("publications_text_100.json", orient='records')
    author_name = df.columns[0]
    df["author"] = str(author_name)
    df["article"] = df[df.columns[0]]
    df = df.drop(columns=[author_name])
    df.reset_index(drop=True,inplace=True)
    v = TfidfVectorizer()
    x = v.fit_transform(df['article'])
    #print(x.toarray())
    df2 = pd.DataFrame(x.toarray().transpose(),
                       index=v.get_feature_names())
    alist=df2.max().tolist()
    new_list = []
    for i in range(len(alist)):
        if i == 50:
            break
        for val in df2[i]:
            if val == alist[i]:
                new_list.append(df2[i].index[df2[i] == val])


    print(new_list)
    #print(df2.columns)
    #return top100(df)

if __name__ == "__main__":
    #mostCommon, _, _ =main()
    #print(mostCommon)
    main()