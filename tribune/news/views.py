from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article
# Create your views here.
def welcome(request):
	return render(request,'welcome.html')

def news_of_day(request):
	date = dt.date.today()
	#FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
	day = convert_dates(date)
	html = f'''
		<html>
			<body>
				<h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
			</body>
			</html>
			'''
	return HttpResponse(html)
	
def convert_dates(dates):
	#function the gets the weekday number for the date.
	day_number = dt.date.weekday(dates)
	days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	#Return the actual day of the week
	day = days[day_number]
	return day

def past_day_news(request,past_date):
	try:
		#Converts data from the string url
		date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
	except ValueError:
		# Raise 404 error when ValueError is thrown
		raise Http404
		assert False

	if date == dt.date.today():
		return redirect(news_today)

	return render(request,'all-news/past-news.html',locals()) 	 	

def news_today(request):
	date =dt.date.today()
	news = Article.todays_news()
	return render(request,'all-news/today-news.html',locals())	

def search_results(request):
	if 'article' in request.GET and request.GET["article"]:
		search_term = request.GET.get("article")
		searched_articles = Article.search_by_title(search_term)
		message = f"{search_term}"
		return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})
	else:
		message='You havent searched for any term'
		return render(request, 'all-news/search.html',locals())		

def article(request,article_id):
	try:
		article = Article.objects.get(id = article_id)
	except DoesNotExist:
		raise Http404()
	return render(request,'all-news/article.html',locals())		