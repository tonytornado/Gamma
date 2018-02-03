from django.shortcuts import render
from django.views import generic

from Warudo.models import Cosplayer


def home(request):
    return render(request, 'home.html')


class ProfileViewer(generic.DetailView):
    model = Cosplayer
    context_object_name = 'cosplayer'
    template_name = 'profile.html'


class ProfileList(generic.ListView):
    model = Cosplayer
    queryset = Cosplayer.objects.all()
    context_object_name = 'cosplayers'
    template_name = 'list-all.html'
