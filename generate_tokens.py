import csv
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

print("Reading input file 'input/audits_with_content.csv'")
with open('input/audits_with_content.csv', 'r') as f:
    reader = csv.reader(f)
    documents = list(reader)

tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

texts = []

print("Generating tokens for every document")
for index, document in enumerate(documents):
    raw_text = document[2].lower()
    tokens = tokenizer.tokenize(raw_text)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    for token in stemmed_tokens:
        texts.append(token)

tokens_set = set(texts)

print("Writing titles into output file")
with open('output/data.tokens', 'w') as f:
    for token in tokens_set:
        print(token, file=f)
