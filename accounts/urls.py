from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_user, name='redirect_user'),

    path('signup/', create_user, name='signup'),
    path('auth/', auth_user, name='auth'),
    path('auth1/', send_code, name = 'send_code'),
    path('login/', login_user, name='login'),
    path('password_reset/', password_reset, name='password_reset'),
    path('login/', login_user, name='login'),
    path('logout/', logout_func, name='logout'),
    path('add_mail/', add_mail, name='add_mail'),
    path('password_reset_2/', password_reset_confirm, name='password_reset_confirm'),
    path('end_pass_reset/', end_pass_reset, name='end_pass_reset'),
    path('users_data/', users_data, name='users_data'),
    path('profile', profile, name='profile'),
]