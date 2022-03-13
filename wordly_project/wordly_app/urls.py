from django.urls import path
from .views import * 

urlpatterns = [
				path('start_play/', StartPlay.as_view()),
				path('play_word/',WordPlayView.as_view()),
				]