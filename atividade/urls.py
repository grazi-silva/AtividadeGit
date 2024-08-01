from django.urls import path
from atividade import views

urlpatterns = [
    path('kayane/', views.view_kayane, name='kayane')
]
