from django.urls import path
from atividade import views

urlpatterns = [
    path('grazi/', views.view_grazi, name='view_grazi'),
    path('kayane/', views.view_kayane, name='kayane'),
]
