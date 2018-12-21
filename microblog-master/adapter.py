from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
# class MyAccountAdapter(DefaultAccountAdapter):
#     def get_login_redirect_url(self, request):
        # return '/'
        # return '/users/{}/'.format(request.user.username)
class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/'
    # def get_logout_redirect_url(self, request):
    #     return '/'
