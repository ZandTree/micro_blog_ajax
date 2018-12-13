# in app views.py

def get_queryset(self,*args,**kwargs):
    # super().get_queryset(*args,**kwargs)
    # в верхнем qs уже отфильтрованные пл twit__isnull?
    posts = Post.objects.filter(twit__isnull=True)
    qs = Post.objects.filter(user=self.request.user)
    return qs
