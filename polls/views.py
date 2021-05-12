from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Post, User_Blog, Comment
from .forms import Post_Form,  Create_User_Form

# def home_view(request):
#     return render(request, "home.html", {})

def create_post_view(request):
    my_form = Post_Form()
    if request.method == "POST":
        my_form = Post_Form(request.POST)
        if(my_form.is_valid()):
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "create_post.html", context)


def home_view(request):
    obj = Post.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "home.html", context)

# def home_view(request):
#     obj = Post.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'content': obj.contents,
#     }
#     return render(request, "home.html", context)

def create_user_view(request):
    new_user_form = Create_User_Form()
    if request.method == "POST":
        new_user_form = Create_User_Form(request.POST)
        if (new_user_form.is_valid()):
            print(new_user_form.cleaned_data)
            User_Blog.objects.create()
        else:
            print(new_user_form.errors)
    context_add_user = {
        "form": new_user_form
    }
    return render(request, "create_user.html", context_add_user)
def posts_list_view(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "posts.html", context)

def post_lookup_view(request, id=id):
    take_post = Post.objects.get(id=id)
    take_coments = Comment.objects.all().filter(post=id)
    context = {
        "post": take_post,
        "coments_list": take_coments
    }
    return render(request, "post_detail.html", context)

def base_page_view(request):
    return render(request, "base.html", {})

def user_table_view(reqest):
    take_table = User_Blog.objects.get(id=id);
    context = {
        "object": take_table
    }
    return render(reqest, "user.html", context)