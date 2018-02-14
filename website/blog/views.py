from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages  as msg
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Post
from .forms import CreatePost
# Create your views here.

def index(request):
    
    user_list = Post.objects.order_by('-pub_date').all()

    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'obj': obj, 'user': user_list })

def create_post(request):
    if not request.user.is_authenticated and not request.user.is_superuser:
        raise Http404
        
    
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            msg.success(request, 'new post created')
            return redirect('blog:index')
    else:
        msg.error(request, 'failed to create post')
        form = CreatePost()
        
    return render(request, 'blog/create.html', {'form': form})


def delete_post(request, post_id=None):
    if not request.user and not request.user.is_superuser:
        raise Http404

    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    msg.success(request, 'Post succesfully deleted')

    return HttpResponseRedirect(reverse('blog:index'))


def edit_post(request, post_id=None):
    if not request.user and not request.user.is_superuser:
        raise Http404

    post_pk = get_object_or_404(Post, pk=post_id)

    var = post_pk.id

    if request.method == 'POST':
        form = CreatePost(request.POST, instance=post_pk)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            msg.success(request, 'Post was succefully edited')
            return HttpResponseRedirect(instance.get_absolute_url())
        
    else:
        msg.error(request, 'Failed to edit post')
        form = CreatePost(instance=post_pk)

    return render(request, 'blog/edit.html', {'form': form, 'post': var})

def post_detail(request, post_id=None):
    instance = get_object_or_404(Post, pk=post_id)

    var = request.build_absolute_uri()

    context = {
        'instance': instance,
        'var': var
    }

    return render(request, 'blog/detail.html', context)
    