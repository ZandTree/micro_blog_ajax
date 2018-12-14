from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.profiles.models import Profile
from backend.app.models import Post
from backend.app.forms import PostForm

class AllPost(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/index.html'
    # paginate_by = 3
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        form = PostForm()
        context['form'] = form
        return context
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.twit = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")

class MyPostView(LoginRequiredMixin,View):
    """"Сообщения пользователя + twits of his(her) followers"""
    def get(self, request):
        posts = self.get_queryset()
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

    def get_queryset(self):
        current_user = self.request.user
        followers_of_current_user = current_user.profile.follower.all()
        lst_id = [current_user.id]
        for id_follower in followers_of_current_user:
            lst_id.append(id_follower)
        qs = Post.objects.filter(user_id__in= lst_id)
        return qs

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.twit = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")

class PostsIfollow(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'app/favorites.html'
    context_object_name = 'posts'

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.twit = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")

    def get_queryset(self):
        current_user = User.objects.get(id = self.request.user.id)
        people_i_follow = current_user.followers.all()
        lst_id = []
        for user in people_i_follow:
            lst_id.append(user.id)
        qs = Post.objects.filter(user_id__in= lst_id)
        return  qs



class Like(LoginRequiredMixin, View):
    """Ставим лайк"""
    def post(self, request):
        pk = request.POST.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)
