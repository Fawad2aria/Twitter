from django.shortcuts import render, reverse, get_object_or_404
from .models import Chirps
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User


def index(request):
    twits = request.user.chirps.all()
    context = {
        'twits': twits
    }

    return render(request, 'posts/index.html', context)

def tweets(request):
    return render(request, 'posts/tweets.html')

def create_chirp(request):
    message = request.POST['message']
    user = request.user
    twit = Chirps(message=message, user=user,created_at=timezone.now())
    twit.save()
    return HttpResponseRedirect(reverse('user_app:home'))

def profile(request, twit_id):
    twit = get_object_or_404(Chirps, pk=twit_id)
    twit.created_at=timezone.now()
    twit.created_at=True
    twit.save()

    return HttpResponseRedirect(reverse('posts:index'))


def likes(request, twit_id):
    obj = get_object_or_404(Chirps, pk=twit_id)
    obj.likes += 1
    obj.save()    
    return HttpResponseRedirect(reverse('user_app:home'))

def user_tweet(request, user_name):
    user = get_object_or_404(User, username=user_name)
    chirps = user.chirps.all()
    context = {
        'chirps': chirps
    }

    return render(request, 'posts/user.html', context)










    

    
    

