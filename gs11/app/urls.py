from django.urls import path,include
from app import views

urlpatterns = [
    path("<str:group_name>", views.index, name = "index")
]
