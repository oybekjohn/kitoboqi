from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
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
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {"login_form": login_form})


    def post(self, request):
        # print(request.POST["username"], request.POST["password"])  datani consoleda print qilib korish
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            
            return redirect("landing_page")
        else:
            return render(request, "users/login.html", {"login_form": login_form})


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        # # shu if kerak emas agarda LoginRequoredMixin dan inheritanse olsak ProfileView classimizga (lekin keyin settingda LOGIN_URL ni korsatib qoyilishimiz kk)
        # if not request.user.is_authenticated:
        #     return redirect("users:login")
        return render(request, "users/profile.html", {"user": request.user})


 