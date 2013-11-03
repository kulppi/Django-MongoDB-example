from django.http import HttpResponse
from django.template import RequestContext, loader
from movies.models import Movies
from django.shortcuts import render

def index(request):
    latest_movie_list = Movies.objects.all()[:5]
    template = loader.get_template('movies/index.html')
    context = RequestContext(request, {
        'latest_movie_list': latest_movie_list,
    })
    return HttpResponse(template.render(context))

def detail(request, pk):
    try:
        movie = Movies.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'movies/detail.html', {'movie': movie})

def results(request, movie_id):
    return HttpResponse("You're looking at the results of movie %s." % movie_id)

def vote(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)