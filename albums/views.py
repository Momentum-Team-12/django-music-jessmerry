from django.shortcuts import render
from .models import Album
from .forms import AlbumForm

# Create your views here.
def add_album(request):
    albums = Album.objects.all()
    return render(request, "albums/home_page.html",
                {"albums": albums})