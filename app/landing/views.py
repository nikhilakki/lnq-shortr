from django.shortcuts import render, redirect
from nanoid import generate
from .forms import URLForm
from .models import URL
# Create your views here.
def home(request):   
    rows = URL.objects.filter(user=request.user)
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.short_url = generate(size=6)
            url.save()
            return redirect('/', pk=url.pk)
    else:
        form = URLForm()
    return render(request, "landing/home.html", {'form': form, 'rows': rows})

def about(request):
    return render(request, "landing/about.html", {})