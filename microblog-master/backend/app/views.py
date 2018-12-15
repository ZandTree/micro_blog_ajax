from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.profiles.models import Profile
from backend.app.models import Post
from backend.app.forms import PostForm
# let op: clas AllPost will be a parent for the others
from django.db.models import Q
from braces.views import PrefetchRelatedMixin

class AllPost(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/index.html'
    #paginate_by = 3
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

# class UserView(PrefetchRelatedMixin, DetailView):
#     model = User
#     prefetch_related = [u"post_set"]  # where the Post model has an FK to the User model as an author.
#     template_name = u"users/detail.html"

class MyPostView(LoginRequiredMixin,AllPost):
    """"Сообщения пользователя + twits of his(her) followers"""
    def get_queryset(self):
        current_user = self.request.user
        #followers_of_current_user = current_user.profile.follower.all()
        followers_of_current_user = current_user.profile.follower.all()
        #1 option (with id's 6 msec)
        lst_id = [current_user.id]
        for id_follower in followers_of_current_user:
            lst_id.append(id_follower)
        qs = Post.objects.filter(user_id__in= lst_id)
        #2 option (Q objects = 8msec)
        #qs = Post.objects.filter(Q(user__in=followers_of_current_user)|Q(user=current_user))
        #3 option select_related
        return qs



class PostsIfollow(LoginRequiredMixin,AllPost):
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

# def get_context_data(self,**kwargs):
#     context = super().get_context_data(**kwargs)
#     context['posts'] = self.get_queryset()
#     return context
# model = Profile
# prefetch_related = ('posts')  # where the Post model has an FK to the User model as an author.
# template_name = u"app/favorites.html"
#
# model = User
# template_name = 'app/favorites.html'
# prefetch_related= [u"user"]

# def get_object(self,queryset=None):
#     obj = get_object_or_404 (
#         User,
#         user = self.request.user
#     )
#     if obj.user != self.request.user:
#         raise Http404
#     return obj
