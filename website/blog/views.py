from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

def index(request):
    
    user_list = Post.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'obj': obj})