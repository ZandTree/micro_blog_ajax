from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from backend.app.models import Post
from backend.app.forms import PostForm


class PostView(View):
    """"Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

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

class Like(View):
    """Ставим лайк"""
    def post(self, request):
        pk = request.POST.get("id")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.obejects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)
