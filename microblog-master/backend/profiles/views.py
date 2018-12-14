from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.views import View
from django.views.generic import UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from backend.app.models import Post


class AddFollower(View):
    """
    blogger gets followers
    """
    def post(self, request):
        pk = request.POST.get("pk")
        # выпилила post id,который приведёт меня к id
        #  blogger I like
        blogger = Profile.objects.get(id=pk)
        fan_id = request.user.id
        fan = User.objects.get(id=fan_id)
        # me прицепляюсь к profile blogger I like
        blogger.follower.add(fan)
        blogger.save()
        return HttpResponse(status=201)


class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_object(self,queryset=None):
        obj = get_object_or_404 (
            Profile,
            user = self.request.user
        )
        if obj.user != self.request.user:
            raise Http404
        return obj

class PublicUserInfo(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/public_user_info.html'

    def get_object(self,queryset=None):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Profile,id=pk)
        return obj

    def get_queryset(self):
        profile = self.get_object()
        user = User.objects.get(id=profile.id)
        qs = user.twits.filter(twit__isnull=True)
        return qs

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context

class ProfileEditView(LoginRequiredMixin,UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self,queryset=None):
        return self.request.user.profile

    def form_valid(self,form):
        messages.success(self.request,'Profile has been updated!')
        return super().form_valid(form)
