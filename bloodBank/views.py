from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'is_signup':False})

def signup_view(request):
    return render(request,'home.html',{'is_signup':True})
