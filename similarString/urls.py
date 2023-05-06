from django.urls import path
from . import views
app_name = 'similarString'
urlpatterns = [
    path('', views.index, name= 'SimilarStringHome'),
    path('findSimilar/', views.findsentence, name= 'FindSimilarSentence'),
]