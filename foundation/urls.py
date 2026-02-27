from django.urls import path
from . import views

app_name = 'foundation'

urlpatterns = [
    path('', views.index, name='index'),
    path('o-fonde/', views.about, name='about'),
    path('program/', views.program, name='program'),
    path('patient-stories/', views.patient_stories, name='patient_stories'),
    path('support/', views.support, name='support'),
]