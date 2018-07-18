from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

urlpatterns=[
url('^$',views.news_today,name = 'welcome'),
url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_day_news,name = 'pastNews'),
url(r'^search/',views.search_results,name='search_results'),
url(r'^article/(?P<article_id>\d+)',views.article,name='article'),
url(r'^new/article$', views.new_article, name='newArticle'),
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)