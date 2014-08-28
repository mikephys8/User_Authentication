from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.


def welcome(request):
    return render_to_response('welcome.html')


# @login_required(login_url='/accounts/login/')
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#             user.save()
#             return HttpResponseRedirect('/admin/')
#         else:
#             # Return a 'disabled account' error message
#             return 'account is disabled'
#     else:
#         # Return an 'invalid login' error message.
#         return 'invalid login'


def login_success(request):
    return render_to_response('login_success.html')