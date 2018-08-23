from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from myblog.models import Post
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


# class BlogIndex(ListView):
#     template_name = 'list.html'
#     context_object_name = 'posts'
#     queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    # model = Post



#@login_required
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)
