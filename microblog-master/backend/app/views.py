from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.profiles.models import Profile
from backend.app.models import Post
from backend.app.forms import PostForm
from django.db.models import Q


class AllPost(View):
    def get(self, request):
        posts = Post.objects.all()
        form = PostForm()
        return render(request, "app/index.html",{"posts":posts,"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.parent = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("/")
        else:
            return HttpResponse("error")



class MyFansPostList(LoginRequiredMixin,View):
    """Сообщения пользователя"""
    def get(self, request):
        # posts = Post.objects.filter(user=request.user)
        posts = Post.objects.filter(
                        Q(user_id__in=self.request.user.profile.get_followers) |
                        Q(user_id=self.request.user.id)
                        )
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts,"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.parent = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("myfans")
        else:
            return HttpResponse("error")



class PostsIFollow(LoginRequiredMixin,View):
    """Вывод твитов тех, кого пользователь отслеживает"""
    def get(self, request):
        current_user = User.objects.get(id = self.request.user.id)
        people_i_follow = current_user.followers.all()
        list_id = current_user.followers.values_list('id',flat=True)
        posts = Post.objects.filter(user_id__in= list_id)
        form = PostForm()
        return render(request, "app/favorites.html", {"posts": posts,"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.parent = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("favorites")
        else:
            return HttpResponse("error")

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
