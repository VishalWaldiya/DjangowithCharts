from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from info import views

urlpatterns = [
    path('api/coord/', views.GraphList.as_view()),
    path('', views.HomeView.as_view(), name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)