from django.shortcuts import render
from apps.kany.models import *

# Create your views here.

def index(requests):
    education = Education.objects.all()
    skill = Skills.objects.all()
    blog = Blog.objects.all()
    experience = Experience.objects.all()
    infouser = UserInfo.objects.latest("id")
    return render(requests, 'index.html', locals())
