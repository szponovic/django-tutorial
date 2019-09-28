from django.shortcuts import render
from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView


# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Byłem w Ryjo, byłem w Bajo, miałem bilet na Hawajo \n'
                        '\tByłem na wsi, byłem w mieście, byłem nawet w Budapeszcie\n'
                        'Wszystko chuj, o ja wam mówię wszystko chuj\n'
                        'O może czasem trochę mniejszy, ale potem jeszcze większy')

def hello_name(request, name):
    return HttpResponse(f'hello {name}!')

def hello_world_template(request):
    return render(request, 'index.html', {})

def simple_list_view(request):
    movies_query = Movie.objects.all()
    return render(request, "list.html", {"movies": movies_query})

class MovieListViev(ListView):
    model = Movie
    template_name = "list.html"
    context_object_name = "movies"

class GenreListViev(ListView):
    model = Genre
    template_name = "list.html"
    context_object_name = "movies"

class PostCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie/add"
    template_name = "add.html"

class PostEditView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "add.html"
    success_url = "/movie_list_by_class_view/"

    # @property
    # def succes_url(self):
    #     #return reverse("movie_list")

class GenreCreateViev(CreateView):
    model = Genre
    form_class =  GenreForm
    success_url = "/genre/add"
    template_name = "add.html"


class GenreEditViev(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "add.html"
    success_url = "/genre_list_by_class_view/"

    # @property
    # def succes_url(self):
    #     return reverse("movie_list")

class PostDeleteViev(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = "/movie_list_by_class_view/"

