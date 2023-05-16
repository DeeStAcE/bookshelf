from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from account.forms import LoginForm


# Create your views here.
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('main')

        return render(request, 'form.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('main')
