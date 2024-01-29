from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Profile


def index(request):
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
