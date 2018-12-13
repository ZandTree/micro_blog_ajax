from django.http import HttpResponse
from django.shortcuts import render, redirect
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

class MyPostView(LoginRequiredMixin,View):
    """"Сообщения пользователя"""
    def get(self, request):
        # if request.user.is_authenticated:
        #posts = Post.objects.filter(twit__isnull=True,user=request.user)
        # else:
        #     posts = Post.objects.filter(twit__isnull=True)
        posts = self.get_queryset()
        form = PostForm()
        return render(request, "app/index.html", {"posts": posts, "form": form})

    def get_queryset(self):
        me = self.request.user
        bloggers_i_follow = me.profile.follower.all()
        # фильтруем последовательно: у поста (должн быть родителeм, а не комментoм)
        # есть юзер - у юзера есть профиль,к напрямую через attr = follow выведет  тех, кого хотим читать
        queryset = Post.objects.filter(twit__isnull=True,user__in=bloggers_i_follow)
        return queryset


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
