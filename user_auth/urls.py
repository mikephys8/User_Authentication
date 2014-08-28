from django.conf.urls import patterns, url
from user_auth import views



urlpatterns = patterns('',

    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^login_success/', views.login_success, name='login_success'),

)
