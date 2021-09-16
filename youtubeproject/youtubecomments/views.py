
from django.shortcuts import render
from django.http import HttpResponse
from .models import Youtubecommment

# Create your views here.
def index(request):
    all_comments = Youtubecommment.objects.all()
    context = {
        'all_comments': all_comments
    }
    return render(request, 'youtubecomments/index.html', context)
