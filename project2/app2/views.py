from django.shortcuts import render
from django.http import HttpResponse
from app2.models import Topic
from app2 import forms

# Create your views here.

#def index(request):
    #return HttpResponse("hello world of avanish")

def index(request):
    topic_list=Topic.objects.all()
    my_dict={"insert_me":topic_list}
    return render(request,"app2/index.html", context=my_dict)
