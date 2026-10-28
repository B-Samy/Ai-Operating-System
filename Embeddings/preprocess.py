from nltk import sent_tokenize 
import re 



def preprocessing_text(text):
    text = text.lower()
    text = re.sub(r'\s+', " " , text)

    return text



