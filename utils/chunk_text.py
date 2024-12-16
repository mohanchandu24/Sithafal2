import nltk
nltk.download('punkt')

def chunk_text(text, chunk_size=200):
    words = nltk.word_tokenize(text)
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
