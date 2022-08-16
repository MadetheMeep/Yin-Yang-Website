from django.urls import path
from . import views, solver

urlpatterns = [
    path('', views.index, name='index'),
    path('answer/', solver.answer, name='answer'),
]