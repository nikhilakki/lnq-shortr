from django.conf import settings
from django.shortcuts import render, redirect
from nanoid import generate
from .form import ShortenURL
from .models import URL

domain = settings.URL_DOMAIN

# Create your views here.
def landing(request):
    if request.method == "POST":
        form = ShortenURL(request.POST)
        if form.is_valid():
            urlForm = form.save(commit=False)
            urlForm.user = request.user
            urlForm.short_url = generate(size=7)
            urlForm.save()
            return redirect("/", pk=urlForm.pk)
    else:
        form = ShortenURL()
        urls = []
        if request.user.is_authenticated:
            urls = URL.objects.filter(user=request.user.id)
    return render(request, "home.html", {"form": form, "urls": urls, "domain": domain})
