from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Editor(models.Model):
	first_name= models.CharField(max_length=30)
	last_name= models.CharField(max_length=30)
	email = models.EmailField()
	phone_number = models.CharField(max_length=10,blank=True)
	def __str__(self):
		return self.first_name
	class Meta:
		ordering = ['first_name']	

	def save_editor(self):
		self.save()	
class tags(models.Model):
	name= models.CharField(max_length=30)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
	def save_tags(self):
		self.save()	

class Article(models.Model):
	title = models.CharField(max_length=60)
	post = HTMLField()
	editor = models.ForeignKey(User)
	tags = models.ManyToManyField(tags)
	pub_date = models.DateTimeField(auto_now_add=True)
	article_image = models.ImageField(upload_to='articles/', blank=True)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['title']
	def save_Article(self):
		self.save()	

	@classmethod
	def todays_news(cls):
		today = dt.date.today()
		news = cls.objects.filter(pub_date__date= today)
		return news

	@classmethod
	def days_news(cls,date):
		news = cls.objects.filter(pub_date_date = date)
		return news	

	@classmethod
	def search_by_title(cls,search_term):
		news = cls.objects.filter(title__icontains=search_term)
		return news	

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
