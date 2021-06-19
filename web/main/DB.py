from .models import Post
from django.core.exceptions import ObjectDoesNotExist

def save(title, data, point, site):
    try:
        movie = Post.objects.get(title=title)
    except Post.DoesNotExist:
        movie = Post.objects.create(title=title, relesedata=data)
    except ObjectDoesNotExist:
        movie = Post.objects.create(title=title, relesedata=data)
    except Exception as ex:
        print("Exception : ", ex)
    if 'RT' == site:
        movie.rt = point
    movie.save()