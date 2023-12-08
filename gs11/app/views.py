from django.shortcuts import render
from .models import Group,Chat
# superuser credential
# admin
# 123
#  igrone favicon save in group model


# Create your views here.
def index(request,group_name):
    print(group_name,"group_name")
    group = Group.objects.filter(name = group_name).first()
    chats = []
    if group:
        pass
    else:
        group = Group(name = group_name)
        group.save()
    return render(request,'app/index.html',{'groupname':group_name, 'chats':chats})
