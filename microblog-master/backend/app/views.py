from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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

# class SignInView(FormView):
#     form_class = SignInForm
#     template_name = 'account/signup.html'
#
#     def form_valid(self, form):
#         bound_form = form.cleaned_data
#         user = auth.authenticate(email=form.user.email, password=bound_form['password'])
#         auth.login(self.request, user)
#         data = dict()
#         data['valid'] = True
#         if self.request.GET.get('next'):
#             data['url'] = self.request.GET.get('next')
#         return HttpResponse(json.dumps(data), content_type="application/json")
