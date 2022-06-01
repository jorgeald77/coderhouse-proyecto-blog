from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Home Blog
from blog.forms import PostCreateForm, CategoryCreateForm
from blog.models import Post, Category, Profile


def index(request):
    last_posts = Post.objects.all().order_by('-created', 'title')[:5]
    return render(request, 'home.html', {'last_posts': last_posts})


# Posts: List, Show, Create, Edit, Delete
def post_list(request):
    posts = Post.objects.all().order_by('-created', 'title')
    return render(request, 'posts/list.html', {'posts': posts})


def post_show(request, pk: int):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/show.html", {'post': post})


def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/listar')

    return render(request, 'posts/create.html', {'form': PostCreateForm})


def post_edit(request):
    pass


def post_delete(request):
    pass


# Categories: List, Show, Create, Edit, Delete
def category_list(request):
    categories = Category.objects.all().order_by('-name')
    return render(request, 'categories/list.html', {'categories': categories})


def category_create(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categories/listar')

    return render(request, 'categories/create.html', {'form': CategoryCreateForm})


def category_edit(request):
    pass


def category_delete(request):
    pass


# Profile: List, Show, Create, Edit, Delete
def profile_list(request):
    profiles = Profile.objects.prefetch_related('user').all()
    return render(request, 'profiles/list.html', {'profiles': profiles})


def profile_show(request, pk: int):
    profile = Profile.objects.get(pk=pk)
    return render(request, "profiles/show.html", {'profile': profile})


def profile_edit(request):
    return HttpResponse("Editar perfil del usuario")
