from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'users/signup.html')

    def post(self, request):
        data = request.POST.dict()
        username, password, confirm_password = data.get('username'), data.get('password'), data.get('confirm_password')
        User.objects.create_user(username=username, password=password)
        if len(username) < 4:
            return render(request, 'users/signup.html', context={'error': 'username should be larger than 4 characters.'})
        elif password != confirm_password:
            return render(request, 'users/signup.html', context={'error': 'passwords are not same'})
        else:
            return HttpResponse('Done')


class Login(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        data = request.POST.dict()
        username, password = data.get('username'), data.get('password')
        users = User.objects.filter(username=username)
        if users and users.first().check_password(password):
            login(request, users.first())
            return HttpResponse('Done')
        else:
            return render(request, 'users/login.html' , context={'error': 'username or password is not correct.'})
        