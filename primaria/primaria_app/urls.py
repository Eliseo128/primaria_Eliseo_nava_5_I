from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.indexvista, name='indexvista'),
    path('mimama/',views.Mi_mama,name="mimama"),

]