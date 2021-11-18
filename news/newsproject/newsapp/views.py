from django.shortcuts import render
import requests
import json




API_KEY='6f6f0e7f557b45bfb5175f1935dbc535'


def index(request):
	country=request.GET.get('country')
	category=request.GET.get('category')
	search_term=request.GET.get('search_term')
	url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
	response=requests.get(url)
	data=response.json()
	articles=data['articles']
	    
	

	
	#print(articles)
	flag=0


	if(search_term !=None):
		flag=1
		url=f'https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}'
		response=requests.get(url)
		data=response.json()
		articles=data['articles']

	
	elif(search_term==None):
		if(country!=None and category!=None):
			flag=1
			url= f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
			response=requests.get(url)
			data=response.json()
			articles=data['articles']
		elif(country!=None):
			flag=1
			url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
			response=requests.get(url)
			data=response.json()
			articles=data['articles']
		elif(category!=None):
			flag=1
			url= f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
			response=requests.get(url)
			data=response.json()
			articles=data['articles']
	
		
	context={
	"articles":articles
	}
	return render(request,'newsapp/index.html',context)

def home(request):
	return render(request,'newsapp/home.html')



