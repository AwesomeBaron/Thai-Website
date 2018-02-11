from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages  as msg
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from .models import Post
from .forms import SeacrhPost
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


    return render(request, 'blog/index.html', {'obj': obj})


@require_POST
def create_post(request):

    if not request.user.is_authenticated and not request.user.is_superuser:
        return Http404

    form = CreatePost(request.POST, request.FILES)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        msg.success(request, 'new post created')
    else:
        msg.error(request, 'failed to create post')

        form = CreatePost()

    return render(request, 'create.html', {'form': form})


def delete_post(request, post_id=None):
    if not request.user and not request.user.is_superuser:
        return Http404

    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    msg.success(request, 'Post succesfully deleted')

    return HttpResponseRedirect(reverse('index'))

@require_POST
def edit_post(request, post_id=None):
    if not request.user and not request.user.is_superuser:
        return Http404
    post = get_object_or_404(Post, pk=post_id)
    form = CreatePost(request.Post, instance=post)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        msg.success(request, 'Post was succefully edited')
        return HttpResponseRedirect(instance.get_absolute_uri())

    else:
        msg.error(request, 'Failed to edit post')
        form = CreatePost(instance=post)

    return render(request, 'edit.html', {'form': form})

def post_detail(request, post_id=None):
    instance = get_object_or_404(Post, pk=post_id)

    context = {
        'instance': instance
    }

    return render(request, 'post_detail.html', context)
    