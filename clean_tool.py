import re
import nltk.corpus
import nltk
import spacy
nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
stop = stopwords.words('english')
    # imports
class clean_text():

    def __init__ (self):
        self.stop = stopwords.words('english')
        self

    def remove_html_tags(self,text):
        """ Removes html tags like "<a> ,<div>" """
        text = re.sub(r'<[^>]+>', r'', text)
        return text

    def remove_special_characters(self,text):
        """ remove all text except [^a-zA-z0-9.,!?/:;\"\'\s]" """
        text = re.sub( r'[^a-zA-z0-9.,!?/:;\"\'\s]', '', text)
        return text

    def remove_punctuation(self,text):
        """ remove !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" """
        for character in string.punctuation:
            text = text.replace(character, '')
        return text
    
    def remove_Unicode(text):
        """ Removes unicode strings like "\u002c" and "x96" """
        text = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', text)       
        text = re.sub(r'[^\x00-\x7f]',r'',text)
        return text

    def remove_URL(text):
        """ Replaces url address with "url" """
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',r'',text)
        return text

    def remove_stopwords(self,text):
        """ Removes stopwords   """
        if text.lower() not in self.stop:
            return text
        else:
            return ""

    def remove_extra_whitespace_tabs(self,text):
        #pattern = r'^\s+$|\s+$'
        text = re.sub(r'^\s*|\s\s*', ' ', text).strip()
        return text
    
    def check_word_length(self,text):
        if len(text)<2:
            return False
        else:
            return True

    def replace_URL(self,text):
        """ Replaces url address with "url" """
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','url',text)
        # text = re.sub(r'#([^\s]+)', r'\1', text)
        return text
        
    def remove_Numbers(self,text):
        """ Removes integers(input:string.word) """
        text = ''.join([i for i in text if not i.isdigit()])         
        return text

    def replaceMultiExclamationMark(self,text):
        """ Replaces repetitions of exlamation marks """
        text = re.sub(r"(\!)\1+", '!', text)
        return text

    def replaceMultiQuestionMark(self,text):
        """ Replaces repetitions of question marks """
        text = re.sub(r"(\?)\1+", '?', text)
        return text

    def replaceMultiStopMark(self,text):
        """ Replaces repetitions of stop marks """
        text = re.sub(r"(\.)\1+", '.', text)
        return text

    def to_lowercase(self,text):
        """ Convert string into lowercase """
        return text.lower()

    def stemmer_nltk(self,text):
        """ Use nltk stemmer to convert string """
        stemmer = nltk.porter.PorterStemmer()
        text = stemmer.stem(text)
        return text 

    def lemmatization_spacy(self,text):
        """ Use nltk stemmer to convert string """
        text = nlp(text)
        text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
        return text
