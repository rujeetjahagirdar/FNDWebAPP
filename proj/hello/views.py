import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Greeting
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.tokenize import RegexpTokenizer
import json
from eventregistry import *
from dandelion import DataTXT

def db(request):

    #greeting = Greeting()
    #greeting.save()

    greetings = Greeting.objects.all()


    return render(request, 'db.html', {'greetings': greetings})

def index(request):
    li=[]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg=request.POST.get('message')
            li=tok1(msg)
            #li1=dan(li,msg)
            return render(request, 'db.html',{'dic1': li})
    else:
        form = ContactForm()
    return render(request, 'index.html',{'form':form})

def tok1(msg):
    lis=[]
    li=[]
    datatxt = DataTXT(app_id='5d504312af124377bac2f69c908dc20b',app_key='5d504312af124377bac2f69c908dc20b')
    repnews=['news.google.co.in','nytimes.com','timesofindia.indiatimes.com','wsj.com','washingtonpost.com','bbc.com','moneycontrol.com','economist.com','newyorker.com','economictimes.indiatimes.com','ndtv.com','indiatoday.in','indianexpress.com','thehindu.com','news18.com','firstpost.com','dnaindia.com','apnews.com','brief.news','npr.org','scroll.in','reuters.com']
    tokenizer = RegexpTokenizer(r'\w+')
    a=tokenizer.tokenize(msg)
    stop = stopwords.words('english') + list(string.punctuation)
    a=[i for i in a if i not in stop]
    er = EventRegistry(apiKey = "e010e4f7-343c-49d5-893d-63d4c2cfd487")
    q = QueryArticlesIter(keywords= QueryItems.OR(a),lang=["eng"],keywordsLoc="title")
    b=q.execQuery(er, sortBy = "rel", maxItems =1 )
    for article in b:
             if(article['source']['uri'] in repnews):
                if article['title'] not in li:
                    lis.append(article['title'])
    for i in range(len(lis)):
        a=datatxt.sim(msg,lis[i])
        if a['similarity'] >= 0.60 :
                print(a['similarity'])
                li.append(lis[i])
    return(li)