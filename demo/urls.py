from django.conf.urls import url

from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^commentsnum/', views.CommentsCount, name='commentscount'),
    url(r'^freq/', views.Frequency, name='freq'),
    # url(r'^d-c-dict/', views.CommentCountHandler, name='d-c-dict'),
    url(r'^emotion/', views.Emotion, name='emotion'),
    url(r'^userlocations/', views.UserLocationRender, name='userlocation'),

]
