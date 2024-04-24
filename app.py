import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

with open('/app/paragraphs.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = re.sub(r'[^\w\s]', '', text).lower()

stop_words = set(stopwords.words('english'))
words = [word for word in text.split() if word not in stop_words]

word_freq = Counter(words)

sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

print("Word frequency count in descending order:")
for word, freq in sorted_word_freq.items():
    print(word, ":", freq)
