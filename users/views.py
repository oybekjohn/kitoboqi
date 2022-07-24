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
            # Save the user without forms
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]

            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)
            user.save()
            return redirect("users:login")
        else:
            context = {
                "form": user_create_form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')