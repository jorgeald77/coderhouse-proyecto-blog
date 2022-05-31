from django.shortcuts import render
from django.http import HttpResponse

# Home Blog
from blog.models import Post


def index(request):
    # Obtener los 5 post mas recientes [:5]
    last_posts = Post.objects.all().order_by('-created', 'title').values()
    return render(request, 'home.html', {'last_posts': last_posts})


# Posts: List, Show, Create, Edit, Delete
def post_list(request):
    return HttpResponse("List Posts")


def post_create(request):
    return HttpResponse("Create Post")


def post_show(request):
    return HttpResponse("Show Post")


def post_edit(request):
    return HttpResponse("Edit Post")


def post_delete(request):
    return HttpResponse("Delete Post")


# Comments: List, Show, Create, Edit, Delete
def comment_list(request):
    return HttpResponse("List Comments")


def comment_create(request):
    return HttpResponse("Create Comment")


def comment_show(request):
    return HttpResponse("Show Comment")


def comment_edit(request):
    return HttpResponse("Edit Comment")


def comment_delete(request):
    return HttpResponse("Delete Comments")


# Users: List, Show, Create, Edit, Delete
def user_list(request):
    return HttpResponse("List Users")


def user_create(request):
    return HttpResponse("Create User")


def user_show(request):
    return HttpResponse("Show User")


def user_edit(request):
    return HttpResponse("Edit User")


def user_delete(request):
    return HttpResponse("Delete User")
