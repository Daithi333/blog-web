from django.contrib.auth import login
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, CommentForm, SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:post_list")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


def post_list(request: HttpRequest) -> HttpResponse:
    """List view for all published blogs, with pagination."""
    posts = Post.objects.filter(published=True).order_by("-created_at")
    paginator = Paginator(posts, 10)  # 10 posts per page

    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """View for a single post and its comments."""
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.order_by("-created_at")  # type: ignore

    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post_detail", slug=post.slug)
    else:
        form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post_detail.html", context)


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    """View for creating a new post."""
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("blog:post_detail", slug=post.slug)
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "blog/post_form.html", context)
