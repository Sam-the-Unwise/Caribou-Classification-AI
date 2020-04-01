from django.urls import path
from . import views
from django.urls import converters

urlpatterns = [

    path('video/', views.targetVideo, name='analysis-targetVideo'),
    path('classification/<video_id>/', views.ResultPrefilled, name='analysis-classification-prefilled'),
    path('category/', views.category, name='analysis-category'),
    path('googleForm/', views.googleForm, name='analysis-googleForm'),

    # path('content/', views.showContent, name='content'),
    path('content/', views.SearchContent, name='content'),

]
