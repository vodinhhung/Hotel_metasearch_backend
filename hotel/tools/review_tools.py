import re
import joblib
from pyvi import ViTokenizer
from nltk.stem import PorterStemmer
import pickle
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
with open('vietnamese_stopwords.txt', encoding="utf8") as f:
    stopwords1 = []
    for line in f:
        stopwords1.append("_".join(line.strip().split()))

with open('vietnamese_stopwords.txt', encoding="utf8") as f:
    stopwords2 = []
    for line in f:
        stopwords2.append(line.strip())
        
stopwords_vi = stopwords1+stopwords2
porter = PorterStemmer()

def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = (re.sub('[\W]+', ' ', text.lower()) + ' ' + ' '.join(emoticons).replace('-', ''))
    
    return text

def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

def preprocessor_vi(text):
    corpus = []
    for i in range(0, len(text)):
        review = re.sub(r"http\S+", "", str(text[i]))
        review = re.sub(r"#\S+", "", review)
        review = re.sub(r"@\S+", "", review)
        review = re.sub('[_]',' ',review)
        review = re.sub('[^a-zA-Z_áàạảãăắằặẵẳâấầẩậẫđíỉìịĩóòỏọõôốồổộỗơớờởợỡéèẹẽẻêếềểệễúùủũụưứừửựữýỳỷỹỵÁÀẢÃẠĂẮẰẲẲẶẴÂẤẦẬẪẨĐÍÌỈỊĨÓÒỎỌÕÔỐỒỔỘỖƠỚỜỞỢỠÉÈẺẸẼÊẾỀỆỂỄÚÙỦŨỤƯỨỪỬỰỮÝỲỶỴỸ]',
                        ' ',review)
        review = ViTokenizer.tokenize(review)
        review = review.lower()
        review = review.split()
        review = [word for word in review if not word in  set(stopwords_vi)]
        review = ' '.join(review)
        corpus.append(review)
    return corpus

def train_review_vi(dataset):
    corpus = preprocessor_vi(dataset)
    tfidf = joblib.load('tfidf.pkl') 
    text_transform = tfidf.transform(corpus)
    classifier = joblib.load('train_review_vi.pkl')
    pred = classifier.predict(text_transform)
    return pred

def train_review_en(dataset):
    classifier = joblib.load('train_review_en.pkl')
    pred = classifier.predict(dataset)
    return pred
