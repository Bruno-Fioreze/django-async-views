from django.http import HttpResponse
import time, asyncio
from movie.models import Movie
from story.models import Story
from asgiref.sync import sync_to_async

def get_movies():
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)

def get_stories():
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)

@sync_to_async
def get_movies_async():
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)

@sync_to_async
def get_stories_async():
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)

def view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('sync')

async def view_async(request):
    start_time = time.time()
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('async')

    # total:  5.002896070480347