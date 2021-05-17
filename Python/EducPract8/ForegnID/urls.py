from django.urls import path
from .views import *

app_name = 'ForeignIDs'
urlpatterns = [
    path('create/', ForeignIDCreateView.as_view()),
    path('all/', ForeignIDCollectionView.as_view()),
    path('detail/<int:pk>', ForeignIDDetailView.as_view()),
]