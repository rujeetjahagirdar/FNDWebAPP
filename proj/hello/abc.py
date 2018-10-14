from newsapi import NewsApiClient
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
a=tokenizer.tokenize(index.msg)

'''newsapi = NewsApiClient(api_key='9d6039a1dcf04f31bfe84d18b6b67737')
my_text = "Donald Trump is on the hunt after reports of a 'resistance' in his ranks"'''
stop = stopwords.words('english') + list(string.punctuation)
a=[i for i in a if i not in stop]
#allart= newsapi.get_everything(q=a[0],language='en')
#print(allart)
print(a)
st=""
for j in range(len(a)):
        if j is not len(a)-1:
            st=st+"'"+a[j]+"'"+" or "
        else:
            st=st+"'"+a[j]+"'"
print(st)
newsapi = NewsApiClient(api_key='9d6039a1dcf04f31bfe84d18b6b67737')
allart= newsapi.get_everything(q=eval(st),language='en')
print(allart)
