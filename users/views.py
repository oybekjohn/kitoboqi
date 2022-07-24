from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserCreateForm
from django.views import View


class RegisterView(View):
    def get(self, request):
        create_user_form = UserCreateForm()
        context = { 
            "form": create_user_form,
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        user_create_form = UserCreateForm(data=request.POST)

        if user_create_form.is_valid():            
            user_create_form.save()
            return redirect("users:login")
        else:
            context = {
                "form": user_create_form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')