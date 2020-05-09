from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from common.debug_utils import debug
from common.views_utils import json_response


def ajax_login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    debug(user)
    response = {}
    if user is not None:
        login(request, user)
        response['is_success'] = True
    elif not User.objects.filter(username=username).exists():
        response['invalid_username'] = True
    else:
        response['invalid_password'] = True
    return json_response(response)


def login_view(request):
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')


@login_required(login_url='/accounts/login')
def change_password_view(request):
    password = request.POST.get('password')
    user = request.user
    user.set_password(password)
    user.save()
    login(request, user)

    return json_response({'is_success': True})
