from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Movie

# Create your views here.
from movies.forms import AddMovie


def movie(request):
    movie = Movie.objects.all()
    data = {"movies" : movie}
    return render(request, 'home.html', data)

def bootstrap(request):
    return render(request, 'bootstrap.html')

def contact(request):
    return render(request, 'contact.html')

def test(request):
    return render(request, 'test.html')


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddMovie(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            release_year = form.cleaned_data['release_year']
            locations = form.cleaned_data['locations']
            production_company = form.cleaned_data['production_company']
            Movie.objects.create(title=title, release_year=release_year, locations=locations, production_company=production_company)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddMovie()

    return render(request, 'add.html', {'form': form})