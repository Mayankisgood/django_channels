from django.urls import path,include
from .views import index

urlpatterns = [
    path("<str:group_name>",index)
]
