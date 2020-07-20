#ici j'ai utilisé ntlk library pour facilité le travail
import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
#------------------------------------------------------------------------------------------------------


#text_cleaning-----------------------------------------------------------------------------------------
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
#------------------------------------------------------------------------------------------------------



#text_tokenization mais ici on utilise word_tokenize à la place de split()-----------------------------
tokenized_words = word_tokenize(cleaned_text, "english")

#supprimer les  Stop_Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization (du pluriel au singulier)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
#------------------------------------------------------------------------------------------------------



#algorithm for emotions--------------------------------------------------------------------------------
emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)
#------------------------------------------------------------------------------------------------------


#positive% & negative%----------------------------------------------------------------------------------
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyse(cleaned_text)
#------------------------------------------------------------------------------------------------------



#emotion graph-----------------------------------------------------------------------------------------
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
#------------------------------------------------------------------------------------------------------