
def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    import re
    import string

    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def preprocess_data(text):
    import nltk
    import nltk
    from nltk.corpus import stopwords

    stemmer = nltk.SnowballStemmer("english")
    stop_words = stopwords.words('english')
    # Clean puntuation, urls, and so on
    text = clean_text(text)
    # Remove stopwords
    text = ' '.join(word for word in text.split(' ') if word not in stop_words)
    # Stemm all the words in the sentence
    text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    
    return text

def fraud_from_description(description) -> str:
    """
    takes in the description of the app and tells whether it is fraud or not 
    :param file: description | str
    :return: boolean
    """
    from keras.models import load_model 
    from nltk.tokenize import word_tokenize
    from keras_preprocessing.sequence import pad_sequences
    from keras.preprocessing.text import Tokenizer
    import pickle 

    with open('tokenizer.pickle', 'rb') as handle:
        word_tokenizer = pickle.load(handle)

    model = load_model("model_desc.h5")
    cleaned_text = preprocess_data(description)

    texts = []
    texts.append(cleaned_text)

    def embed(corpus): 
        return word_tokenizer.texts_to_sequences(corpus)

    longest_train = max(texts, key=lambda sentence: len(word_tokenize(sentence)))
    length_long_sentence = len(word_tokenize(longest_train))

    train_padded_sentences = pad_sequences(
        embed(texts), 
        length_long_sentence, 
        padding='post'
    )

    y_preds = (model.predict(train_padded_sentences) > 0.5).astype("int32")
    return y_preds
