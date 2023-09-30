from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import Sum, Max, Min, Count, Avg


# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.order_by(
        'name')  # order_by делает сортировку по имени, если поставить -name, сортировка в обратном,
    # можно делать срезы order_by('rating')[:5], сортировать несколько столбцов order_by('name', 'budget'))
    # for movie in movies:
    #     movie.save()
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('name'))
    return render(request, 'movie_app/movie_all.html',
                  {
                   'movies': movies,
                   'agg': agg,
                   })


# def show_one_movie(request, id_movie: int):
#     movie = get_object_or_404(Movie, id=id_movie) #этот метод 404 возвращает страницу нот фаунд. Можно было без этого метода(Movie.objects.get(id=id_movie)
#     return render(request, 'movie_app/one_movie.html',
#                   {'movie': movie})
def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie,
                              slug=slug_movie)  # этот метод 404 возвращает страницу нот фаунд. Можно было без этого метода(Movie.objects.get(id=id_movie)
    return render(request, 'movie_app/one_movie.html',
                  {'movie': movie})
